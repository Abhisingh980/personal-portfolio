from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=1000,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    html_url = models.URLField(null=True, blank=True)
    readme = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
