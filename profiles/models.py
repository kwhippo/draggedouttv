from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    author = models.ForeignKey(User, related_name='profile')
