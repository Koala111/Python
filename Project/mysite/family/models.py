from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 20)
    def __str__(self):
        return self.name

class Hobby(models.Model):
    hobby = models.ForeignKey(Family, on_delete = models.CASCADE)
    kind = models.CharField(max_length = 200)
    def __str__(self):
        return self.kind



    


