from django.contrib import admin
from contests import models as m
# Register your models here.
admin.site.register(m.Contest)
admin.site.register(m.ContestEntry)
