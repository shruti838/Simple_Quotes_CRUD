from django.db import models

# Create your models here.

class Quote(models.Model):                                  #create Quote table
    text = models.TextField(max_length=255)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.text 