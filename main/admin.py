from django.contrib import admin

from .models import Category, News  , Comment

# Register your models h


class AdminNews(admin.ModelAdmin):
    list_display = ['title','title',]

class AdminComments(admin.ModelAdmin):
    list_display = ['name','email','status',]

admin.site.register(Category)
admin.site.register(News,AdminNews)
admin.site.register(Comment ,AdminComments)