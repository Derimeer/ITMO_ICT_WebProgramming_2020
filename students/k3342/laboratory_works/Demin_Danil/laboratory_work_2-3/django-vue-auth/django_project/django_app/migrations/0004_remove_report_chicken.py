# Generated by Django 3.0.8 on 2020-09-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20200814_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='chicken',
        ),
    ]
