from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.text} - ({self.post_date}) - ({self.author.username})'
