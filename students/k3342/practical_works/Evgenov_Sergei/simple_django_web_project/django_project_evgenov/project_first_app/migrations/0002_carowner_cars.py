# Generated by Django 3.0.5 on 2020-06-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Car'),
        ),
    ]
