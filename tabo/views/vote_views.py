from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Posting, Comment_P, Co_Comment_P


@login_required(login_url='common:login')
def vote_posting(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)
    if request.user == posting.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        posting.voter.add(request.user)
    return redirect('tabo:detail', posting_id=posting.id)


# 현재 댓글과 대댓글의 추천 기능은 사용하지 않음


@login_required(login_url='common:login')
def vote_comment_p(request, comment_p_id):
    comment_p = get_object_or_404(Comment_P, pk=comment_p_id)
    if request.user == comment_p.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        comment_p.voter.add(request.user)
    return redirect('tabo:detail', posting_id=comment_p.posting.id)


@login_required(login_url='common:login')
def vote_co_comment_p(request, co_comment_p_id):
    co_comment_p = get_object_or_404(Co_Comment_P, pk=co_comment_p_id)
    if request.user == co_comment_p.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        co_comment_p.voter.add(request.user)
    return redirect('tabo:detail', posting_id=co_comment_p.comment_p.posting.id)