# Generated by Django 5.0.1 on 2024-02-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]