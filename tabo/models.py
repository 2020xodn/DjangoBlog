from django.db import models
from django.contrib.auth.models import User


class Posting(models.Model):    # 게시글
    tag = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_posting')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_posting')
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


    def update_hits(self):
        self.hits = self.hits + 1
        self.save()
        return self.hits


class Photo(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class File(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)


class Comment_P(models.Model):  # 게시글의 댓글
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment_p')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_comment_p')

    def __str__(self):
        return self.content


class Co_Comment_P(models.Model):  # 게시글의 대댓글
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_co_comment_p')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    comment_p = models.ForeignKey(Comment_P, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_co_comment_p')

    def __str__(self):
        return self.content