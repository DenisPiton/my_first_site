# Generated by Django 4.2.11 on 2024-03-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0005_remove_item_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default='a', max_length=10000),
        ),
    ]
