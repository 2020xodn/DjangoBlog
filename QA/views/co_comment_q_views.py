from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import Co_Comment_Q_Form
from ..models import Question, Comment_Q, Co_Comment_Q

from .commonMethod import canDelete


@login_required(login_url='common:login')
def co_comment_q_create(request, comment_q_id):
    comment_q = get_object_or_404(Comment_Q, pk=comment_q_id)
    if request.method == "POST":
        form = Co_Comment_Q_Form(request.POST)
        if form.is_valid():
            co_comment_q = form.save(commit=False)
            co_comment_q.author = request.user
            co_comment_q.create_date = timezone.now()
            co_comment_q.comment_q = comment_q
            co_comment_q.save()
            return redirect('{}#co_comment_q_{}'.format(
                resolve_url('QA:detail', question_id=comment_q.question.id), co_comment_q.id))
    else:
        form = Co_Comment_Q_Form()
    context = {'form': form, 'question_id': comment_q.question.id}
    return render(request, 'QA/co_comment_q_form.html', context)


@login_required(login_url='common:login')
def co_comment_q_modify(request, co_comment_q_id):
    co_comment_q = get_object_or_404(Co_Comment_Q, pk=co_comment_q_id)
    if request.user != co_comment_q.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('QA:detail', question_id=co_comment_q.comment_q.question.id)

    if request.method == "POST":
        form = Co_Comment_Q_Form(request.POST, instance=co_comment_q)
        if form.is_valid():
            co_comment_q = form.save(commit=False)
            co_comment_q.author = request.user
            co_comment_q.modify_date = timezone.now()
            co_comment_q.save()
            #return redirect('QA:detail', question_id=co_comment_q.comment_q.question.id)
            return redirect('{}#co_comment_q_{}'.format(
                resolve_url('QA:detail', question_id=co_comment_q.comment_q.question.id), co_comment_q.id))
    else:
        form = Co_Comment_Q_Form(instance=co_comment_q)
    context = {'form': form}
    return render(request, 'QA/co_comment_q_form.html', context)


@login_required(login_url='common:login')
def co_comment_q_delete(request, co_comment_q_id):
    co_comment_q = get_object_or_404(Co_Comment_Q, pk=co_comment_q_id)
    if request.user != co_comment_q.author and not canDelete(request):
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('QA:detail', question_id=co_comment_q.comment_q.question.id)
    else:
        co_comment_q.delete()
    return redirect('QA:detail', question_id=co_comment_q.comment_q.question.id)