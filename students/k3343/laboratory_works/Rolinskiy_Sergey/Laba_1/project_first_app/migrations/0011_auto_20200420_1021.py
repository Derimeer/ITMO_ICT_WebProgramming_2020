# Generated by Django 3.0.4 on 2020-04-20 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0010_auto_20200420_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='din',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dout',
        ),
    ]
