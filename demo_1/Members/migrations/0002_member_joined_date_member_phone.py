# Generated by Django 4.1.4 on 2022-12-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
