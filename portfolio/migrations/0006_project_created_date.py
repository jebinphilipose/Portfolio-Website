# Generated by Django 2.1.2 on 2020-07-18 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200718_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]