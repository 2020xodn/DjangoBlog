from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Posting
from ..forms import New_Tag_Form

from utils.tagList import tagList


def show_tags(request):
    posting_list = Posting.objects.order_by('-create_date')

    number = [posting_list.filter(tag=t).count() for t in tagList]

    result = [[tagList[i], number[i]] for i in range(len(tagList))]

    groupList = []
    for values in request.user.groups.values_list():
        groupList.append(values[1])

    context = {'tags': result, 'posting_list': posting_list, 'groupList': groupList, 'tag_list': tagList}
    return render(request, 'tag/tag_page.html', context)


# 기술 부족으로 폐기
# def add_tag(request):
#     for values in request.user.groups.values_list():    # 직접 주소에 입력해서 들어왔을 경우
#         if values[1] == 'Manager':
#             break
#     else:
#         return redirect('tabo:show_tags')
#     print(1)
#     if request.method == 'POST':
#         form = New_Tag_Form(request.POST)
#         if form.is_valid():
#             tagList.remove(form.Meta.fields)
#             return redirect('tabo:show_tags')
#     else:
#         pass
#         form = New_Tag_Form()
#     context = {'form': form}
#     return render(request, 'tag/add_tag.html', context)