# Generated by Django 5.1.3 on 2024-12-18 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0020_remove_processeddata_valor_total'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProcessedData',
            new_name='Gasto',
        ),
    ]
