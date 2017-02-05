"""test51 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf import settings

from cms import views as cms_views

urlpatterns = [
    url(r'^$', cms_views.home, name='home'),
    url(r'^(?P<page>[0-9]+)/$', cms_views.home, name='home'),
    url(r'^(?P<page>[0-9]+)/(?P<tag>[0-9]+)/$', cms_views.home, name='home'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', cms_views.profile, name='profile'),
    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
