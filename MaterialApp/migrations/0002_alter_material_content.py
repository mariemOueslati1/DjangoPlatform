# Generated by Django 4.2.5 on 2023-12-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.FileField(upload_to='materials/'),
        ),
    ]
