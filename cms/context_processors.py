from cms.models import Page, Tag

def menu_data(request):
    pages = Page.objects.all()
    tags = Tag.objects.all()
    return {'tags': tags, 'pages': pages}
