# Generated by Django 3.2.4 on 2021-06-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20210612_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='replies',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
