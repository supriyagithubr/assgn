from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField()

