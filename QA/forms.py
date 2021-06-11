from django import forms
from .models import Question, Comment_Q, Co_Comment_Q


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['tag', 'subject', 'content']

        labels = {
            'tag': '태그',
            'subject': '제목',
            'content': '내용',
        }


class Comment_Q_Form(forms.ModelForm):
    class Meta:
        model = Comment_Q
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class Co_Comment_Q_Form(forms.ModelForm):
    class Meta:
        model = Co_Comment_Q
        fields = ['content']
        labels = {
            'content': '대댓글내용',
        }