# Generated by Django 2.2 on 2019-04-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_list_dateadded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created_at',
            field=models.DateField(),
        ),
    ]