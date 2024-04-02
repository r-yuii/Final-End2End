from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # timestamp
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    progress = models.CharField(max_length=100)
    score = models.CharField(max_length=2)
  
