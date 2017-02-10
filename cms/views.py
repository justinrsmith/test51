from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from allauth.socialaccount.models import SocialAccount

from cms.models import Post, Page, Tag, Game, Competition, Match

# Get either an individual post via /page/slug or get a list
# of posts for the page
@login_required
def get_post_or_posts(request, page=None, slug=None):
    # Get the page object and all related post sorted by
    # date created, if the page does not exist return them to
    # home page
    try:
        page = Page.objects.get(slug__iexact=page)
        posts = Post.objects.filter(page=page).order_by('-date_created')
        # If home page get all post by date desc
        if page.is_home_page:
            posts = Post.objects.order_by('-date_created')
        elif slug:
            posts = posts.filter(slug__iexact=slug)
    except Page.DoesNotExist:
        # Get home page
        page = Page.objects.get(is_home_page=True)
        # If no page return them to home page
        return redirect('/'+page.slug)
    return render(request, 'index.html', {
        'posts': posts,
        'page': page.id
    })

@login_required
def get_tag(request, tag):
    tag = get_object_or_404(Tag, title__iexact=tag)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'index.html', {
        'posts': posts,
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

@login_required
def add_match(request):
    matches = Match.objects.all()
    games = Game.objects.all()
    match = Match.objects.first()

    return render(request, 'add_matchjq.html', {
        'matches': matches,
        'games': games
    })
