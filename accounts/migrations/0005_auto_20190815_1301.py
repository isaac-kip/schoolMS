# Generated by Django 2.1.7 on 2019-08-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190815_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastudent',
            name='FatherDesignation',
            field=models.CharField(default='text', max_length=100),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='FatherName',
            field=models.CharField(default='text', max_length=100),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='FatherPhone',
            field=models.CharField(default='text', max_length=100),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='FatherProfession',
            field=models.CharField(default='text', max_length=100),
        ),
    ]