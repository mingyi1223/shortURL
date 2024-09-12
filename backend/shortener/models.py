from django.db import models

# Create your models here.

class Site(models.Model):
  long = models.URLField()
  short = models.URLField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)