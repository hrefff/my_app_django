from django.contrib import admin
from blog.models import Article, Image

# Register your models here.

# admin.site.register(Article)
# admin.site.register(Image)

class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Article

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

