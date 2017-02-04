from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cms.models import Post

@login_required
def home(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'index.html', {
        'posts': posts
    })
