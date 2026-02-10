from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MediaItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # ForeignKey 
    created_date = models.DateTimeField(default=timezone.now) # DateTimeField 
    author_or_director = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    item = models.ForeignKey(MediaItem, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author} on {self.item}'
    class Meta:
        unique_together = ('item', 'author')