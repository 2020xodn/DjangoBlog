from django import forms
from tabo.models import Posting, Comment_P, Co_Comment_P, New_Tag


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['tag', 'subject', 'content']

        labels = {
            'tag': '태그',
            'subject': '제목',
            'content': '내용',
        }


class Comment_P_Form(forms.ModelForm):
    class Meta:
        model = Comment_P
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class Co_Comment_P_Form(forms.ModelForm):
    class Meta:
        model = Co_Comment_P
        fields = ['content']
        labels = {
            'content': '대댓글내용',
        }


class New_Tag_Form(forms.ModelForm):
    class Meta:
        model = New_Tag
        fields = ['content']
        labels = {
            'content': '태그이름',
        }