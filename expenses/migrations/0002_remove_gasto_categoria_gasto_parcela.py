# Generated by Django 5.1.3 on 2024-12-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='gasto',
            name='parcela',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
