# Generated by Django 3.0.6 on 2020-06-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport_app', '0003_arrivaldeparture_plane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenger',
            name='is_hired',
            field=models.BooleanField(default=False),
        ),
    ]
