# Generated by Django 3.1.2 on 2020-10-30 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('colour', models.CharField(max_length=40)),
                ('state_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_of_ownership', models.DateField()),
                ('finish_date_of_ownership', models.DateField()),
                ('car_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('own_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_of_issue', models.DateField()),
                ('type', models.CharField(choices=[('A', 'Motorcycle'), ('B', 'Van'), ('C', 'Car'), ('D', 'Bus'), ('M', 'Motorcar')], max_length=10)),
                ('own_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
    ]