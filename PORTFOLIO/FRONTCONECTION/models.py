
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    html_url = models.URLField(max_length=1000)
    readme = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['title','html_url'])
        ]

class Contact(models.Model):
    name = models.CharField(max_length=1000,null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    position = models.CharField(max_length=1000,null=True, blank=True)
    phone_number = models.CharField(max_length=1000,null=True, blank=True)
    message = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['email'])
        ]
