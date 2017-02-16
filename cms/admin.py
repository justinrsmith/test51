from django.contrib import admin
from django import forms
from django.utils.text import slugify
from cms import models as m


class PostForm(forms.ModelForm):
    def clean_slug(self):
        title = self.cleaned_data.get('title', None)
        slug = self.cleaned_data.get('slug', None)
        page = self.cleaned_data.get('page', None)
        # If user does not provide a slug, slugify the title and
        # validate against that
        if not slug:
            slug = slugify(title)
        try:
            slug_check = m.Post.objects.get(slug=slug)
            # If we get an object and it is same id as the current
            # instance being and the slug is the same then we
            # don't need to validate
            if slug_check.id == self.instance.id and slug_check.slug==slug:
                return slug
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


class PageForm(forms.ModelForm):
    def clean_is_home_page(self):
        is_home_page = self.cleaned_data.get('is_home_page', None)
        if is_home_page:
            try:
                home_page_exists = m.Page.objects.get(is_home_page=True)
                raise forms.ValidationError('The page %s is already marked as home page.' % home_page_exists.title)
            except m.Page.DoesNotExist:
                return is_home_page

    class Meta:
        model = m.Page
        fields = '__all__'

class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ('title', 'created_by', 'date_created')
    exclude = ('created_by', 'date_created', 'slug',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


class MatchAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/admin/js/custom_admin.js',)


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('handle', 'first_name', 'last_name',)


class TeamPlayerAdmin(admin.ModelAdmin):
    raw_id_fields = ['player',]
    list_display = ('player', 'team', 'active')

# Register your models here.
admin.site.register(m.Post, PostAdmin)
admin.site.register(m.Page, PageAdmin)
admin.site.register(m.Tag)
admin.site.register(m.Game)
admin.site.register(m.Competition)
admin.site.register(m.Team)
admin.site.register(m.Player, PlayerAdmin)
admin.site.register(m.TeamPlayer, TeamPlayerAdmin)

admin.site.register(m.Map)


admin.site.register(m.Match)
admin.site.register(m.MatchMap)
admin.site.register(m.MatchMapTeamResult)
