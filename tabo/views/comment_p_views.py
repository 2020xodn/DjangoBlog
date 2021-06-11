from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import Comment_P_Form
from ..models import Posting, Comment_P

from .commonMethod import canDelete


@login_required(login_url='common:login')
def comment_p_create(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)

    if request.method == "POST":
        form = Comment_P_Form(request.POST)
        if form.is_valid():
            comment_p = form.save(commit=False)
            comment_p.create_date = timezone.now()
            comment_p.posting = posting
            comment_p.author = request.user
            comment_p.save()
            #return redirect('tabo:detail', posting_id=posting.id)
            return redirect('{}#comment_p_{}'.format(
                resolve_url('tabo:detail', posting_id=posting.id), comment_p.id))
    else:
        form = Comment_P_Form()
    context = {'posting': posting, 'form': form}
    return render(request, 'tabo/posting_detail.html', context)


@login_required(login_url='common:login')
def comment_p_modify(request, comment_p_id):
    comment_p = get_object_or_404(Comment_P, pk=comment_p_id)
    if request.user != comment_p.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('tabo:detail', posting_id=comment_p.posting.id)

    if request.method == "POST":
        form = Comment_P_Form(request.POST, instance=comment_p)
        if form.is_valid():
            comment_p = form.save(commit=False)
            comment_p.author = request.user
            comment_p.modify_date = timezone.now()
            comment_p.save()
            #return redirect('tabo:detail', posting_id=comment_p.posting.id)
            return redirect('{}#comment_p_{}'.format(
                resolve_url('tabo:detail', posting_id=comment_p.posting.id), comment_p.id))
    else:
        form = Comment_P_Form(instance=comment_p)
    context = {'comment_p': comment_p, 'form': form}
    return render(request, 'tabo/comment_p_form.html', context)


@login_required(login_url='common:login')
def comment_p_delete(request, comment_p_id):
    comment_p = get_object_or_404(Comment_P, pk=comment_p_id)
    if request.user != comment_p.author and not canDelete(request):
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment_p.delete()
    return redirect('tabo:detail', posting_id=comment_p.posting.id)