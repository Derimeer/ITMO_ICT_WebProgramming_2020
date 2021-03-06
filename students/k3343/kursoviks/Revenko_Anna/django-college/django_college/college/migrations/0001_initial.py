# Generated by Django 3.0.6 on 2020-05-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_num', models.IntegerField()),
                ('passport_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_points', models.IntegerField()),
                ('common_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('free_positions', models.IntegerField()),
                ('applications_num', models.IntegerField()),
                ('minimal_point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecializationRealise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Department')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_class', models.CharField(choices=[('1', '9'), ('2', '11')], default='1', max_length=1)),
                ('privelege', models.CharField(choices=[('1', 'No'), ('2', 'Disabled'), ('3', 'Orphan')], default='1', max_length=1)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('certificate_avg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Certificate')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Document')),
                ('exams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Faculty'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(choices=[('1', 'Accepted'), ('2', 'Not accepted'), ('3', 'In process')], default='3', max_length=1)),
                ('education_form', models.CharField(choices=[('1', 'Contract'), ('2', 'Budget')], default='1', max_length=1)),
                ('enrollee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Enrollee')),
                ('secretary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Secretary')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Specialization')),
            ],
        ),
    ]
