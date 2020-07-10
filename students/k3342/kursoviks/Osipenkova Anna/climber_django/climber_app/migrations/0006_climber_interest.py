# Generated by Django 3.0.7 on 2020-06-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climber_app', '0005_climber_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='climber',
            name='interest',
            field=models.CharField(choices=[('1', 'Skiing'), ('2', 'Ice hockey'), ('3', 'Soccer'), ('4', 'Basketball'), ('5', 'Hockey'), ('6', 'Reading'), ('7', 'Writing')], default='1', max_length=1),
        ),
    ]
