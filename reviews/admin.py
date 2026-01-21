from django.contrib import admin
from .models import Category, MediaItem, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_or_director', 'created_date')
    search_fields = ('title', 'author_or_director')
    list_filter = ('category',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'author', 'rating', 'published_date')
    list_filter = ('rating', 'published_date')