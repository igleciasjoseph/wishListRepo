# Generated by Django 2.2 on 2019-04-25 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='dateadded',
        ),
    ]
