from django.db import models

# Create your models here.


class ScrapeRequest(models.Model):
    email = models.EmailField()
    csv_path = models.CharField(max_length=100)
    result_csv_path = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)