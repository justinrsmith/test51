from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from cms.models import Post, Page, Tag
from allauth.socialaccount.models import SocialAccount

@login_required
def home(request):
    posts = Post.objects.all().order_by('-date_created')
    pages = Page.objects.all()
    tags = Tag.objects.all()
    page = Page.objects.get(title='Home')
    return render(request, 'index.html', {
        'posts': posts,
        'pages': pages,
        'tags': tags,
        'page': page.id
    })

def get_page(request, page):
    if page=='home':
        return redirect('/')
    #TODO: iexact gives case insensitve search
    page = get_object_or_404(Page, slug__iexact=page)
    posts = Post.objects.filter(page=page).order_by('-date_created')
    pages = Page.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'pages': pages,
        'tags': tags,
        'page': page.id
    })

def get_post(request, page, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    pages = Page.objects.all()
    tags = Tag.objects.all()
    return render(request, 'post.html', {
        'post': post,
        'pages': pages,
        'tags': tags
    })

def get_tag(request, tag):
    tag = get_object_or_404(Tag, title__iexact=tag)
    posts = Post.objects.filter(tags=tag)
    pages = Page.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'pages': pages,
        'tags': tags,
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
