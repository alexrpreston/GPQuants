from django.db import models

# Create your models here.

class covidHeadlines(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
