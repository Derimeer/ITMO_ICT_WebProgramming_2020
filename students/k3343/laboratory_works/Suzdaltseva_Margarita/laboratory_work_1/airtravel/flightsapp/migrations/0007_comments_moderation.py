# Generated by Django 3.0.5 on 2020-04-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightsapp', '0006_commentcategory_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]