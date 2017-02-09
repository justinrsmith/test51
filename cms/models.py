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
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Map(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    handle = models.CharField(max_length=30)

    def __str__(self):
        return self.handle


class Team(models.Model):
    name = models.CharField(default='Area 51', max_length=20)
    game = models.ForeignKey(Game)
    # TODO show only active players
    active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s - %s' % (self.name, self.game.abbreviation)


class TeamPlayer(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    active = models.BooleanField(default=True)


class Competition(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Match(models.Model):
    competition = models.ForeignKey(Competition)
    date = models.DateField()
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2')
    team1_roster = models.ManyToManyField(Player, related_name='team1_roster')
    team2_roster = models.ManyToManyField(Player, related_name='team2_roster')


class Result(models.Model):
    match = models.ForeignKey(Match)
    map = models.ForeignKey(Map)
    team1_1st_score = models.IntegerField()
    team1_2nd_score = models.IntegerField()
    team1_ot_score = models.IntegerField()
    team2_1st_score = models.IntegerField()
    team2_2nd_score = models.IntegerField()
    team2_ot_score = models.IntegerField()
