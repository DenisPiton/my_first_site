# Generated by Django 4.2.8 on 2024-03-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='href',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='a', max_length=1000),
        ),
    ]