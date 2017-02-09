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
import cms.rest_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/(?P<user_id>[0-9]+)/$', cms_views.profile, name='profile'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(cms.rest_api.router.urls)),
    url(r'^add_match/', cms_views.add_match, name='add_match'),
    url(r'^tags/(?P<tag>[\w\-]+)/$', cms_views.get_tag, name='get_tag'),
    # User can hit /
    url(r'^$', cms_views.get_post_or_posts, name='get_post_or_posts'),
    # Page slug /home/
    url(r'^(?P<page>[\w\-]+)/$', cms_views.get_post_or_posts, name='get_post_or_posts'),
    # Get direct article use page slug with post slug for readable url
    url(r'^(?P<page>[\w\-]+)/(?P<slug>[\w\-]+)/$', cms_views.get_post_or_posts, name='get_post_or_posts'),
]

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
