from django.db import models
from redactor.fields import RedactorField
from django.utils import timezone
from django.contrib.auth.models import User


class Page(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


# Create your models here.
class Post(models.Model):
    page           = models.ForeignKey(Page)
    title          = models.CharField(max_length=40)
    content        = RedactorField()
    author         = models.ForeignKey(User, null=True, blank=True)
    date_published = models.DateTimeField(default=timezone.now)
    tags           = models.ManyToManyField(Tag, null=True, blank=True)
    date_created   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
