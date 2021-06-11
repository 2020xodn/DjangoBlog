from django.urls import path

from .views import base_views, posting_views, comment_p_views, co_comment_p_views, vote_views, tagSearch_views, info_views, main_views


app_name = 'tabo'


urlpatterns = [
    # tabo
    # base_views
    path('', base_views.index, name='index'),
    path('<int:posting_id>/', base_views.detail, name='detail'),

    # posting_views
    path('posting/create/', posting_views.posting_create, name='posting_create'),
    path('posting/modify/<int:posting_id>/', posting_views.posting_modify, name='posting_modify'),
    path('posting/delete/<int:posting_id>/', posting_views.posting_delete, name='posting_delete'),

    # comment_p_views
    path('comment_p/create/<int:posting_id>/', comment_p_views.comment_p_create, name='comment_p_create'),
    path('comment_p/modify/<int:comment_p_id>/', comment_p_views.comment_p_modify, name='comment_p_modify'),
    path('comment_p/delete/<int:comment_p_id>/', comment_p_views.comment_p_delete, name='comment_p_delete'),

    # co_comment_p_views
    path('co_comment_p/create/comment_p/<int:comment_p_id>/', co_comment_p_views.co_comment_p_create, name='co_comment_p_create'),
    path('co_comment_p/modify/comment_p/<int:co_comment_p_id>/', co_comment_p_views.co_comment_p_modify, name='co_comment_p_modify'),
    path('co_comment_p/delete/comment_p/<int:co_comment_p_id>/', co_comment_p_views.co_comment_p_delete, name='co_comment_p_delete'),

    # vote_views.py
    path('vote/posting/<int:posting_id>/', vote_views.vote_posting, name='vote_posting'),
    path('vote/comment_p/<int:comment_p_id>/', vote_views.vote_comment_p, name='vote_comment_p'),
    path('vote/co_comment_p/<int:co_comment_p_id>/', vote_views.vote_co_comment_p, name='vote_co_comment_p'),

    # main_views.py
    path('main/', main_views.show_main, name='show_main'),

    # tagSearch_views.py
    path('tag/', tagSearch_views.show_tags, name='show_tags'),

    # info_views.py
    path('info/', info_views.show_info, name='show_info'),


]