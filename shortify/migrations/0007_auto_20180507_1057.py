# Generated by Django 2.0.4 on 2018-05-07 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortify', '0006_auto_20180507_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userurl',
            name='page_desc',
        ),
        migrations.RemoveField(
            model_name='userurl',
            name='page_title',
        ),
    ]