from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Enter field documentation')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    created_date = models.DateTimeField()
    publshed_date = models.DateTimeField()