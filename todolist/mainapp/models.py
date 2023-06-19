from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    time_creation = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False)


class Rubric(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
