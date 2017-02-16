from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from allauth.socialaccount import models as all_auth_models

# Create your models here.
class Contest(models.Model):
    name = models.CharField(max_length=50)
    #description
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #header graphic
    #show entries

class ContestEntry(models.Model):
    contest = models.ForeignKey(Contest)
    full_name = models.CharField(max_length=55)
    email = models.CharField(max_length=75)
    user = models.ForeignKey(User, null=True, blank=True)
    datetime_submitted = models.DateTimeField(default=timezone.now)
    social_provider = models.CharField(max_length=30, blank=True, null=True)
