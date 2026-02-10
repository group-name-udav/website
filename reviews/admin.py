from django.contrib import admin
from .models import Category, MediaItem, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_or_director', 'image_thumbnail', 'created_date')
    search_fields = ('title', 'author_or_director')
    list_filter = ('category',)
    
    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="75" />'
        return 'No Image'
    image_thumbnail.short_description = 'Thumbnail'
    image_thumbnail.allow_tags = True

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'author', 'rating', 'published_date')
    list_filter = ('rating', 'published_date')