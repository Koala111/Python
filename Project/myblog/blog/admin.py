from django.contrib import admin
from blog.models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content']


admin.site.register(Article)