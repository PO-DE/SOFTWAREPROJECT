# Generated by Django 5.0.1 on 2024-04-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_hotels_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='city',
        ),
        migrations.AddField(
            model_name='activities',
            name='description',
            field=models.CharField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]
