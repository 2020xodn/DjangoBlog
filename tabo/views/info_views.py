from django.shortcuts import render, get_object_or_404


def show_info(request):
    info_data = [
        ["이름", "내이름"],
        ["학과", "컴공"],
        ["학번", "17~"],
        ["분야", "Java, Unity"],
        ["메일", "bbpasd@gmail.com"],
        ["깃허브", "https://github.com/2020xodn"],
        ["작성일", "21-06-06"],
    ]

    context = {'info_data': info_data}
    return render(request, 'info/info_page.html', context)