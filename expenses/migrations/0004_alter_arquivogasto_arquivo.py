# Generated by Django 5.1.3 on 2024-12-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_arquivogasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivogasto',
            name='arquivo',
            field=models.FileField(upload_to='assets/csv/'),
        ),
    ]