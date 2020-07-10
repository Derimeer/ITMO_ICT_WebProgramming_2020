# Generated by Django 3.0.7 on 2020-06-30 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_auto_20200623_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='enrollee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='college.Enrollee'),
        ),
        migrations.AlterField(
            model_name='ege',
            name='enrollee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ege', to='college.Enrollee'),
        ),
    ]