from django.db import models


# Create your models here.
class Item(models.Model):
    img_source = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    created_by = models.CharField(max_length=30)
    description.default = "a"
    created_by.default = ""

