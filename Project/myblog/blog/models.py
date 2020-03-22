from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 32, default = 'Title')
    content = models.TextField(null = True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

    def __str__(self):
        return self.title