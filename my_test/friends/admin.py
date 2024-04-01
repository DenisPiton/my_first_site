from django.contrib import admin

# Register your models here.
from .models import Item, Comments

admin.site.register(Item)
admin.site.register(Comments)