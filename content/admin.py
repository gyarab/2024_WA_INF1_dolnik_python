from django.contrib import admin
from .models import Game, Category, Author, Comment


class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    #list_filter = ['category']
    date_hierarchy = 'published'
    search_fields = ['title', 'perex', 'text']

# Register your models here.
admin.site.register(Game,GameAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)