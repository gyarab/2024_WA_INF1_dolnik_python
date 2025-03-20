from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)
    
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Game(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    text = models.TextField()
    published = models.DateTimeField()
    categories = models.ManyToManyField(Category, related_name='games')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='games')
    votes_sum=models.IntegerField(default=0)
    votes_count=models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)
class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    time = models.DateTimeField(auto_now_add=True, null=True)
    ip=models.GenericIPAddressField(default=None, null=True)
    user_agent = models.CharField(max_length=200, default=None, null=True)
    def __str__(self):
        return str(self.name)
