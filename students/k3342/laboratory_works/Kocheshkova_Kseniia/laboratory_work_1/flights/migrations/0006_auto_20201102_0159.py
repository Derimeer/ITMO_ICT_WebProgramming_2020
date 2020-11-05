# Generated by Django 3.1.2 on 2020-11-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20201102_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='full_name',
            field=models.CharField(default='Marina', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='passport_number',
            field=models.IntegerField(default='37461523'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone_number',
            field=models.IntegerField(default='63428'),
            preserve_default=False,
        ),
    ]