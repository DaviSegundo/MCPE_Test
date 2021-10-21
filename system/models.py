from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    cod = models.IntegerField(primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.description

class Process(models.Model):
    cod = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title