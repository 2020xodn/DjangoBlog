from django.shortcuts import render, get_object_or_404

from ..models import Posting


def show_tags(request):

    posting_list = Posting.objects.order_by('-create_date')

    tags = ["C",
            "Java",
            "Python",
            "HTML",
            "etc",
    ]

    number = [posting_list.filter(tag=t).count() for t in tags]

    result = [[tags[i], number[i]] for i in range(len(tags))]


    context = {'tags': result, 'posting_list': posting_list}
    return render(request, 'tag/tag_page.html', context)