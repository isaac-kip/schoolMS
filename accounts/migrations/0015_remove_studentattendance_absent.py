# Generated by Django 2.1.7 on 2019-08-16 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_studentattendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentattendance',
            name='Absent',
        ),
    ]