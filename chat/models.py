from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from glean import settings


class Theme(models.Model):
    """テーマ"""
    authid = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作成者', related_name='theme')
    theme = models.CharField('テーマ', max_length=255)
    text = models.TextField('説明', blank=True)
    is_enforce = models.BooleanField(default=False)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.theme

    def __str_comment__(self):
        return self.comment

    def __update__(self):
        return self.updatedate


class Comment(models.Model):
    """コメント"""
    comment = models.TextField('コメント', blank=False)
    authid = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', related_name='comment')
    themeid = models.ForeignKey(Theme, verbose_name='投稿先', related_name='comment')
    createdate = models.DateTimeField(auto_now_add=True)
    good = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
