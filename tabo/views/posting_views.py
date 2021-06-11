from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User

from ..forms import PostingForm
from ..models import Posting

from utils.commonMethod import canDelete


@login_required(login_url='common:login')
def posting_create(request):
    for values in request.user.groups.values_list():    # 직접 주소에 입력해서 들어왔을 경우
        if values[1] == 'canPosting':
            break
    else:
        return redirect('tabo:index')

    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.author = request.user
            posting.create_date = timezone.now()
            posting.save()
            return redirect('tabo:index')
    else:
        form = PostingForm()
    context = {'form': form}
    return render(request, 'tabo/posting_form.html', context)


@login_required(login_url='common:login')
def posting_modify(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)
    if request.user != posting.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('tabo:detail', posting_id=posting.id)

    if request.method == "POST":
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.modify_date = timezone.now()  # 수정일시 저장
            posting.save()
            return redirect('tabo:detail', posting_id=posting.id)
    else:
        form = PostingForm(instance=posting)
    context = {'form': form}
    return render(request, 'tabo/posting_form.html', context)


@login_required(login_url='common:login')
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)
    if request.user != posting.author and not canDelete(request):
        messages.error(request, '삭제권한이 없습니다')
        return redirect('tabo:detail', posting_id=posting.id)

    posting.delete()
    return redirect('tabo:index')