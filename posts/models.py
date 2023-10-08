from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

'''
- title
- author
- content
- image
- publish_data
- tags
'''

'''
- fields
- html wieghts
- validation
'''


class post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)\
        # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title
