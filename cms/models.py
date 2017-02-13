from django.db import models
from redactor.fields import RedactorField
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from collections import defaultdict, Counter


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
    is_area_51 = models.BooleanField(default=False)

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
    team = models.ForeignKey(Team, related_name='team')
    team_roster = models.ManyToManyField(TeamPlayer, related_name='team_roster')
    opponent = models.ForeignKey(Team, related_name='opponent')
    opponent_roster = models.ManyToManyField(TeamPlayer, related_name='opponent_roster')
    datetime_submitted = models.DateTimeField(default=timezone.now)

    def get_maps(self):
        return len(self.matchmap_set.all())

    # Get the winner of a match regardless of maps play
    def get_results(self):
        # Get all the maps in the set
        match_maps = self.matchmap_set.all()
        results = []
        for mm in match_maps:
            # Dictionary to hold map result data
            result = {}
            # Get the map
            result['map'] = mm.map
            for team_result in mm.matchmapteamresult_set.all():
                final_score = (team_result.first_half_score
                               +team_result.second_half_score
                               +team_result.overtime_score)
                # Build score info for map for team and opponent
                # Dyanmically build key name to cut down on code
                key_type = 'team'
                if not team_result.team.is_area_51:
                    key_type = 'opponent'
                result[key_type] = team_result.team
                result[key_type+'_first_half_score'] = team_result.first_half_score
                result[key_type+'_second_half_score'] = team_result.second_half_score
                result[key_type+'_final_score'] = final_score
            results.append(result)
        # If match is a series
        if len(results)>1:
            # Intialize dict just in case no one wins a map, since they
            # won't get returned using Counter collection
            result={}
            result['team'] = self.team
            result['team_final_score'] = 0
            result['opponent'] = self.opponent
            result['opponent_final_score'] = 0
            # If a team won a map add them to the list of winers
            winners = []
            for r in results:
                if r['team_final_score'] > r['opponent_final_score']:
                    winners.append(r['team'])
                else:
                    winners.append(r['opponent'])
            # Get the count of times a team one then build the result dict
            for k,v in Counter(winners).most_common():
                if k.is_area_51:
                    result['team_final_score'] = v
                else:
                    result['opponent_final_score'] = v
        # Mark who the winner was
        if result['team_final_score'] > result['opponent_final_score']:
            result['winner'] = result['team']
        elif result['team_final_score'] < result['opponent_final_score']:
            result['winner'] = result['opponent']
        return result


class MatchMap(models.Model):
    match = models.ForeignKey(Match)
    map = models.ForeignKey(Map)

    def __str__(self):
        return self.map.name


class MatchMapTeamResult(models.Model):
    match_map = models.ForeignKey(MatchMap)
    # TODO need a better name need to decide on naming convention
    # team for a51 vs opponent
    # team seems to vague to use as 51 team field
    team = models.ForeignKey(Team)
    first_half_score = models.IntegerField()
    second_half_score = models.IntegerField()
    overtime_score = models.IntegerField()
