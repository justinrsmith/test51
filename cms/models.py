from django.db import models
from redactor.fields import RedactorField
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


class Page(models.Model):
    title        = models.CharField(max_length=100, unique=True)
    # show to user?
    slug         = models.SlugField(blank=True, unique=True)
    is_home_page = models.BooleanField(default=False)
    created_by   = models.ForeignKey(User, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

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
    slug           = models.SlugField(blank=True, unique=True)
    content        = RedactorField()
    author         = models.ForeignKey(User, null=True, blank=True)
    date_published = models.DateTimeField(default=timezone.now)
    tags           = models.ManyToManyField(Tag, blank=True)
    date_created   = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if  not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Game(models.Model):
    pass


class Team(models.Model):
    pass


class Match(models.Model):
    pass
