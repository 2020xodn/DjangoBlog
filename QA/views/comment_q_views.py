from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import Comment_Q_Form
from ..models import Question, Comment_Q

from utils.commonMethod import canDelete


@login_required(login_url='common:login')
def comment_q_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = Comment_Q_Form(request.POST)
        if form.is_valid():
            comment_q = form.save(commit=False)
            comment_q.create_date = timezone.now()
            comment_q.question = question
            comment_q.author = request.user
            comment_q.save()
            return redirect('{}#comment_q_{}'.format(
                resolve_url('QA:detail', question_id=question.id), comment_q.id))
    else:
        form = Comment_Q_Form()
    context = {'question': question, 'form': form}
    return render(request, 'QA/question_detail.html', context)


@login_required(login_url='common:login')
def comment_q_modify(request, comment_q_id):
    comment_q = get_object_or_404(Comment_Q, pk=comment_q_id)
    if request.user != comment_q.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('QA:detail', question_id=comment_q.question.id)

    if request.method == "POST":
        form = Comment_Q_Form(request.POST, instance=comment_q)
        if form.is_valid():
            comment_q = form.save(commit=False)
            comment_q.author = request.user
            comment_q.modify_date = timezone.now()
            comment_q.save()
            return redirect('{}#comment_q_{}'.format(
                resolve_url('QA:detail', question_id=comment_q.question.id), comment_q.id))
    else:
        form = Comment_Q_Form(instance=comment_q)
    context = {'comment_q': comment_q, 'form': form}
    return render(request, 'QA/comment_q_form.html', context)


@login_required(login_url='common:login')
def comment_q_delete(request, comment_q_id):
    comment_q = get_object_or_404(Comment_Q, pk=comment_q_id)
    if request.user != comment_q.author and not canDelete(request):
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment_q.delete()
    return redirect('QA:detail', question_id=comment_q.question.id)