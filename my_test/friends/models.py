from django.db import models


# Create your models here.
class Item(models.Model):
    img_source = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    created_by = models.CharField(max_length=30)
    description.default = "a"
    created_by.default = ""
    tag = models.CharField(max_length=200)
    tag.default = "other food"
    ingredients = models.CharField(max_length=2000)
    ingredients.default= ""
    image = models.ImageField(upload_to="images")
    image.default = ""


class Comments(models.Model):
    created_by = models.CharField(max_length=255)
    comment_text = models.TextField()
    related_to = models.ForeignKey(Item, on_delete=models.CASCADE)
class test_image_upload(models.Model):
    image = models.ImageField(upload_to="images/")
