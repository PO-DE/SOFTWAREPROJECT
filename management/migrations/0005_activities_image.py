# Generated by Django 5.0.1 on 2024-04-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_remove_activities_city_activities_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='image',
            field=models.ImageField(default=' ', upload_to='activity_images/'),
            preserve_default=False,
        ),
    ]
