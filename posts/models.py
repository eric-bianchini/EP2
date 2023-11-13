from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Título Padrão")
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title} - ({self.text}) - ({self.date}) - ({self.author.username})'
