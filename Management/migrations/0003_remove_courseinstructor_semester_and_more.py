# Generated by Django 4.0.1 on 2022-02-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_alter_instructor_instrustor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinstructor',
            name='semester',
        ),
        migrations.AddField(
            model_name='courseinstructor',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='courseinstructor',
            name='year',
        ),
        migrations.AddField(
            model_name='courseinstructor',
            name='year',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='studentsection',
            name='semester',
        ),
        migrations.AddField(
            model_name='studentsection',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='studentsection',
            name='year',
        ),
        migrations.AddField(
            model_name='studentsection',
            name='year',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
