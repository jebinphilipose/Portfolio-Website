# Generated by Django 2.1 on 2018-09-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180916_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
