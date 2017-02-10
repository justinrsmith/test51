from django.db import models
from redactor.fields import RedactorField
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from collections import defaultdict


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
    
    def get_maps(self):
        return len(self.matchmap_set.all())

    # Get the winner of a match regardless of maps play
    def get_winner(self):
        # Get all the maps in the set
        match_maps = self.matchmap_set.all()
        # Dictionary to hold the results of the series by map
        results = {}
        # Dict that will be used to store the number of map wins by team
        maps_won = {}
        for mm in match_maps:
            # Get the results for the map
            results[mm.map] = {}
            for result in mm.matchmapteamresult_set.all():
                # Build map final score for team
                final_score = (result.first_half_score
                               + result.second_half_score
                               + result.overtime_score)
                # Initate the maps_won for team to be 0
                maps_won[result.team] = 0
                results[mm.map][result.team] = final_score
        for k,v in results.items():
            if v:
                # Get team who had highest score for map
                max_key = max(v, key=lambda k: v[k])
                # Increment maps won
                maps_won[max_key] += 1
        # Get who had the most maps won
        max_key = max(maps_won, key=lambda k: maps_won[k])
        return max_key


class MatchMap(models.Model):
    match = models.ForeignKey(Match)
    map = models.ForeignKey(Map)

    def __str__(self):
        return self.map.name


class MatchMapTeamResult(models.Model):
    match_map = models.ForeignKey(MatchMap)
    team = models.ForeignKey(Team)
    fielded_roster = models.ManyToManyField(TeamPlayer)
    first_half_score = models.IntegerField()
    second_half_score = models.IntegerField()
    overtime_score = models.IntegerField()

#class TeamResult(models.Model):
    #match_team = models.MatchTeam(MatchTeam)

#    team = models.ForeignKey(Team)


    #def team_score(self):
    #    team_score = self.first_half_score + self.second_half_score + overtime_score
    #    return team_score
