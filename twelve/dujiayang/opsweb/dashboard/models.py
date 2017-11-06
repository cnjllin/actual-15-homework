#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    name            = models.CharField('中文名', max_length=32)
    phone           = models.CharField('手机', max_length=11, null=True, blank=True)
    wechat          = models.CharField('微信', max_length=32, null=True, blank=True)
    title           = models.CharField('职位', max_length=32, null=True, blank=True)
    class Meta:
        db_table = "user_profile"
        verbose_name = 'user'
    def __unicode__(self):
        return self.username


