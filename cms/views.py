from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from cms.models import Post, Page, Tag
from allauth.socialaccount.models import SocialAccount

@login_required
def home(request, page=None, tag=None):
    if not page:
        return redirect('/1')
    if tag:
        tag_obj = Tag.objects.get(pk=tag)
        posts = Post.objects.filter(tags=tag_obj)
        tag=int(tag)
    else:
        posts = Post.objects.filter(page_id=page).order_by('-date_created')
    pages = Page.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'pages': pages,
        'tags': tags,
        'page': int(page),
        'tag': tag
    })

@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    twitch_acct = False
    # Get social account of user
    try:
        sa = SocialAccount.objects.get(user=user)
        if sa.provider == 'twitch':
            twitch_acct = True
    except:
        pass

    return render(request, 'profile.html', {
        'user': user,
        'twitch_acct': twitch_acct
    })
