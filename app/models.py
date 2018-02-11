from django.db import models

# Create your models here.


class ScrapeRequest(models.Model):
    email = models.EmailField()
    csv_path = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
