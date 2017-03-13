from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatar/', null=True)


class Category(models.Model):
    title = models.TextField()
    extended_info = models.TextField()
    logo = models.ImageField(upload_to='category_logo/', null=True)

    def __unicode__(self):
        return self.title


class Thread(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    thread = models.ForeignKey(Thread, null=True)
    title = models.TextField(null=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    def as_dict(self):
        return {
            'text': self.text,
            'author': str(self.author),
        }

    def __unicode__(self):
        return self.text

