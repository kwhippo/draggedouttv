from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Profile(models.Model):
    author = models.OneToOneField(User)
    drag_name = models.CharField(blank=False, null=False, max_length=50)
    given_name = models.CharField(blank=True, null=True, max_length=50)
    name_origin = models.TextField(blank=True, null=True, max_length=150)
    likes = TaggableManager()
    about = models.TextField(blank=True, null=True, max_length=250)
