from django.db import models
from redactor.fields import RedactorField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    content = RedactorField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title

class Game(models.Model):
    name = models.CharField(max_length=20)

class Team(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Game)

    def __str__(self):
        return '%s - %s' % (self.name, self.game.name)
