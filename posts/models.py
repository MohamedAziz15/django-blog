from django.db import models

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
    title = models.CharField(max_length=100)\
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField() 

    




