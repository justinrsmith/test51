from django.contrib import admin

from cms import models as m

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

# Register your models here.
admin.site.register(m.Post, PostAdmin)
admin.site.register(m.Page)
admin.site.register(m.Tag)
