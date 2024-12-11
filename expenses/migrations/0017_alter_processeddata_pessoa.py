# Generated by Django 5.1.3 on 2024-12-10 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0016_processeddata_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processeddata',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.pessoa'),
        ),
    ]
