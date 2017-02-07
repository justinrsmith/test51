from django.contrib import admin
from django import forms
from django.utils.text import slugify
from cms import models as m


class PostForm(forms.ModelForm):
    def clean_slug(self):
        title = self.cleaned_data.get('title', None)
        slug = self.cleaned_data.get('slug', None)
        # If user does not provide a slug, slugify the title and
        # validate against that
        if not slug:
            slug = slugify(title)
        try:
            slug_check = m.Post.objects.get(slug=slug)
        except m.Post.DoesNotExist:
            return slug
        if slug_check:
            raise forms.ValidationError('%s already exists as a slug, please set a custom slug' % slug)


    class Meta:
        model = m.Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'date_created',)
    exclude = ('author', 'date_created',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'date_created')
    exclude = ('created_by', 'date_created', 'slug',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

# Register your models here.
admin.site.register(m.Post, PostAdmin)
admin.site.register(m.Page, PageAdmin)
admin.site.register(m.Tag)
