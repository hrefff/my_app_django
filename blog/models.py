from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.article.title
