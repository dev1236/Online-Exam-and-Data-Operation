# Generated by Django 3.0.8 on 2021-05-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineclass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_submit',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
