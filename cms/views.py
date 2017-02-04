from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from cms.models import Post
from allauth.socialaccount.models import SocialAccount

@login_required
def home(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'index.html', {
        'posts': posts
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
