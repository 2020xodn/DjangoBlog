from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.utils import timezone
from django.contrib.auth.models import User

from ..models import Question

import datetime


def QAList(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    # tags = request.GET.get('tags', '')

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('comment_q')).order_by('-num_answer', '-create_date')
    elif so == 'hits':
        question_list = Question.objects.order_by('-hits', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')


    # 검색
    if kw:
        question_list = question_list.filter(
            Q(tag=kw) |  # 태그는 정확히
            Q(subject__icontains=kw) |  # 제목
            Q(content__icontains=kw) |  # 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment_q__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    today = timezone.now()

    # user = User.objects.all()
    groupList = []
    for values in request.user.groups.values_list():
        groupList.append(values[1])

    commentNum = []
    for question in page_obj:
        tmp = 0
        for comment in question.comment_q_set.all():
            tmp += comment.co_comment_q_set.count() + 1

        commentNum.append(tmp)

    question_commentNum = [[page_obj[i], commentNum[i]] for i in range(len(page_obj))]

    context = {'question_list': question_commentNum, 'page': page, 'kw': kw, 'so': so, 'today': today, 'groupList': groupList, 'page': page_obj}
    return render(request, 'QA/QA_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    today = timezone.now()
    groupList = []
    for values in request.user.groups.values_list():
        groupList.append(values[1])

    commentNum = question.comment_q_set.count()
    for comment in question.comment_q_set.all():
        commentNum = commentNum + comment.co_comment_q_set.count()

    context = {'question': question, 'today': today, 'groupList': groupList, 'commentNum': commentNum}
    return render(request, 'QA/question_detail.html', context)