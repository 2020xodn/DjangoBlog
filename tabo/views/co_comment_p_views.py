from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import Co_Comment_P_Form
from ..models import Posting, Comment_P, Co_Comment_P

from .commonMethod import canDelete


@login_required(login_url='common:login')
def co_comment_p_create(request, comment_p_id):
    comment_p = get_object_or_404(Comment_P, pk=comment_p_id)
    if request.method == "POST":
        form = Co_Comment_P_Form(request.POST)
        if form.is_valid():
            co_comment_p = form.save(commit=False)
            co_comment_p.author = request.user
            co_comment_p.create_date = timezone.now()
            co_comment_p.comment_p = comment_p
            co_comment_p.save()
            #return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)
            return redirect('{}#co_comment_p_{}'.format(
                resolve_url('tabo:detail', posting_id=comment_p.posting.id), co_comment_p.id))
    else:
        form = Co_Comment_P_Form()
    context = {'form': form, 'posting_id': comment_p.posting.id}
    return render(request, 'tabo/co_comment_p_form.html', context)


@login_required(login_url='common:login')
def co_comment_p_modify(request, co_comment_p_id):
    co_comment_p = get_object_or_404(Co_Comment_P, pk=co_comment_p_id)
    if request.user != co_comment_p.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)

    if request.method == "POST":
        form = Co_Comment_P_Form(request.POST, instance=co_comment_p)
        if form.is_valid():
            co_comment_p = form.save(commit=False)
            co_comment_p.author = request.user
            co_comment_p.modify_date = timezone.now()
            co_comment_p.save()
            #return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)
            return redirect('{}#co_comment_p_{}'.format(
                resolve_url('tabo:detail', posting_id=co_comment_p.comment_p.posting.id), co_comment_p.id))
    else:
        form = Co_Comment_P_Form(instance=co_comment_p)
    context = {'form': form}
    return render(request, 'tabo/co_comment_p_form.html', context)


@login_required(login_url='common:login')
def co_comment_p_delete(request, co_comment_p_id):
    co_comment_p = get_object_or_404(Co_Comment_P, pk=co_comment_p_id)
    if request.user != co_comment_p.author and not canDelete(request):
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)
    else:
        co_comment_p.delete()
    return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)
