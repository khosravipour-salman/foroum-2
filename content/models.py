from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.db import models
from django.urls import reverse
from django.conf import settings


# from myauth.models import UserModel


class PostModel(models.Model):
    STATUS = (
        ('locked', 'Locked'),
        ('open', 'Open')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post',
                             default=None)
    title = models.CharField(max_length=64)
    # slug = models.SlugField(max_length=250, default=None)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=6, default='open')
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('mycontent:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

    def get_date(self):
        return humanize.naturaltime(self.updated)

    def __str__(self):
        return self.title


class AnswerModel(models.Model): # modelname_set
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer', default=None)
    abody = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    image = models.ImageField()
    accepted = models.BooleanField()

    def __str__(self):
        return self.abody


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_comment', null=True)
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE, related_name='answer_comment', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', default=None)
    cbody = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_date(self):
        return humanize.naturaltime(self.created, self.updated)

    def __str__(self):
        return self.cbody
