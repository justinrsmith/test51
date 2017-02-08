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
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    handle = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.handle


class Team(models.Model):
    name = models.CharField(default='Area 51', max_length=20)
    game = models.ForeignKey(Game)
    # Don't require players to be added to field
    # TODO show only active players
    players = models.ManyToManyField(Player, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.game.abbreviation)


class Competition(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    map = models.ForeignKey(Map)
    map_number = models.IntegerField()
    team_score = models.IntegerField()
    opposing_score = models.IntegerField()

    def __str__(self):
        return '%s - %s %s Map-%s' % (
            self.team_score, self.opposing_score, self.map, self.map_number
        )


class Match(models.Model):
    MATCH_RESULTS = (
        ('W', 'Win'),
        ('L', 'Loss'),
        ('D', 'Draw'),
    )
    MATCH_TYPES = (
        ('BO1', 'Best of 1'),
        ('BO3', 'Best of 3'),
        ('BO5', 'Best of 5'),
        ('BO7', 'Best of 7'),
    )
#    match_type = models.CharField(choices=MATCH_TYPES, max_length=3, default='BO1')
    competition = models.ForeignKey(Competition)
    #map = models.ForeignKey(Map)
    match_date = models.DateField(default=timezone.now)
    team = models.ForeignKey(Team)
    opponent = models.CharField(max_length=20)
    results = models.ManyToManyField(Result)
    #team_score = models.IntegerField()
    #opposing_score = models.IntegerField()
    #result = models.CharField(choices=MATCH_RESULTS, max_length=2)

    def __str__(self):
        return '%s vs %s at %s' % (
            self.team.name, self.opponent, self.competition.name
        )
