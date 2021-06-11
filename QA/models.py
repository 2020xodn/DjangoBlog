from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):    # 질문
    tag = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


    def update_hits(self):
        self.hits = self.hits + 1
        self.save()
        return self.hits


class Comment_Q(models.Model):  # 질문의 댓글
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment_q')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_comment_q')

    def __str__(self):
        return self.content


class Co_Comment_Q(models.Model):  # 질문의 대댓글
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_co_comment_q')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    comment_q = models.ForeignKey(Comment_Q, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_co_comment_q')

    def __str__(self):
        return self.content