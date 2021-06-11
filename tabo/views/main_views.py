from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from ..models import Posting


def show_main(request):

    posting_list = Posting.objects.order_by('-create_date')
    recent_list = posting_list[0:5]
    today = timezone.now()
    context = {'recent_list': recent_list, 'today': today}
    return render(request, 'main/main_page.html', context)