from django.contrib import admin
from .models import Article, Category


# Register your models here.

admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):   
    list_display = ('title', 'published', 'category')
    list_display_links = ('title', 'published')
    list_filter = ('published', 'category')   
    date_hierarchy = 'published'
    search_fields = ('title', 'perex', 'text')

admin.site.register(Article, ArticleAdmin)