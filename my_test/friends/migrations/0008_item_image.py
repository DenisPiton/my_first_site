# Generated by Django 4.2.11 on 2024-03-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0007_item_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]