from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default=" ")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}, Content: {self.content}, Author: {self.author}'
