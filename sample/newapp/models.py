from django.db import models

# Create your models here.

class dispmodel(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    def __str__(self):
        return self.title
