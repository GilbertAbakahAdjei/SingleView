from django.db import models

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=200)
    work_count = models.IntegerField(default=1)

class Work(models.Model):
    file_id = models.IntegerField()
    title = models.CharField(max_length=200)
    contributors = models.CharField(max_length=200)
    iswc = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    proprietary_id = models.IntegerField()


    # work_count = models.IntegerField(default=1) 
    

