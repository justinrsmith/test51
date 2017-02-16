from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from allauth.socialaccount import models as all_auth_models

def graphic_file_path(instance, imagename):
    # file will be uploaded to MEDIA_ROOT/<contest.name>/<imagename>/
    return '{0}/{1}'.format(instance.name, imagename)

# Create your models here.
class Contest(models.Model):
    name = models.CharField(max_length=50)
    graphic = models.ImageField(upload_to=graphic_file_path, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
        

class ContestEntry(models.Model):
    contest = models.ForeignKey(Contest)
    full_name = models.CharField(max_length=55)
    email = models.CharField(max_length=75)
    user = models.ForeignKey(User, null=True, blank=True)
    datetime_submitted = models.DateTimeField(default=timezone.now)
    social_provider = models.CharField(max_length=30, blank=True, null=True)
