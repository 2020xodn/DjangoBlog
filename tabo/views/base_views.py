from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.utils import timezone
from django.contrib.auth.models import User

from ..models import Posting

import datetime


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    searchTag = request.GET.get('searchTag', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    # tags = request.GET.get('tags', '')

    # 정렬
    if so == 'recommend':
        posting_list = Posting.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        posting_list = Posting.objects.annotate(num_answer=Count('comment_p')).order_by('-num_answer', '-create_date')
    elif so == 'hits':
        posting_list = Posting.objects.order_by('-hits', '-create_date')
    else:  # recent
        posting_list = Posting.objects.order_by('-create_date')


    # 검색
    if kw:
        posting_list = posting_list.filter(
            Q(tag=kw) |  # 태그는 정확히
            Q(subject__icontains=kw) |  # 제목
            Q(content__icontains=kw) |  # 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment_p__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    if searchTag:   # 오직 태그 검색
        posting_list = posting_list.filter(
            Q(tag=searchTag)  # 태그는 정확히
        ).distinct()

    paginator = Paginator(posting_list, 12)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    today = timezone.now()

    # user = User.objects.all()
    groupList = []
    for values in request.user.groups.values_list():
        groupList.append(values[1])

    commentNum = []
    for posting in page_obj:
        tmp = 0
        for comment in posting.comment_p_set.all():
            tmp += comment.co_comment_p_set.count() + 1

        commentNum.append(tmp)

    posting_commentNum_reImage = [
        [page_obj[i], commentNum[i], page_obj[i].photo_set.all()[0]]
        if len(page_obj[i].photo_set.all()) != 0 else [page_obj[i], commentNum[i], None]
        for i in range(len(page_obj))
    ]


    context = {'posting_list': posting_commentNum_reImage, 'page': page, 'kw': kw, 'so': so,
               'today': today, 'groupList': groupList, 'page': page_obj, 'posting_num': len(posting_list), 'renderPostingNum': len(page_obj)}
    return render(request, 'tabo/posting_list.html', context)


def detail(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)
    today = timezone.now()
    groupList = []
    for values in request.user.groups.values_list():
        groupList.append(values[1])

    commentNum = posting.comment_p_set.count()
    for comment in posting.comment_p_set.all():
        commentNum = commentNum + comment.co_comment_p_set.count()

    context = {'posting': posting, 'today': today, 'groupList': groupList, 'commentNum': commentNum}
    return render(request, 'tabo/posting_detail.html', context)