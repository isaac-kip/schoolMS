# Generated by Django 2.1.7 on 2019-08-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190815_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastudent',
            name='Father_Photo',
            field=models.ImageField(default='text', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='Mother_Photo',
            field=models.ImageField(default='text', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='Student_Photo',
            field=models.ImageField(default='text', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='datastudent',
            name='Transfer_Certificate',
            field=models.ImageField(default='text', upload_to='gallery'),
        ),
    ]