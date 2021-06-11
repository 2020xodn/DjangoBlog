from django.urls import path

from QA.views import QA_views, question_views, comment_q_views, co_comment_q_views, vote_views

app_name = 'QA'

urlpatterns = [
    # QA_views.py
    path('', QA_views.QAList, name='QAList'),
    path('<int:question_id>/', QA_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # comment_q_views
    path('comment_q/create/<int:question_id>/', comment_q_views.comment_q_create, name='comment_q_create'),
    path('comment_q/modify/<int:comment_q_id>/', comment_q_views.comment_q_modify, name='comment_q_modify'),
    path('comment_q/delete/<int:comment_q_id>/', comment_q_views.comment_q_delete, name='comment_q_delete'),

    # co_comment_q_views
    path('co_comment_q/create/comment_q/<int:comment_q_id>/', co_comment_q_views.co_comment_q_create, name='co_comment_q_create'),
    path('co_comment_q/modify/comment_q/<int:co_comment_q_id>/', co_comment_q_views.co_comment_q_modify, name='co_comment_q_modify'),
    path('co_comment_q/delete/comment_q/<int:co_comment_q_id>/', co_comment_q_views.co_comment_q_delete, name='co_comment_q_delete'),

    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
]