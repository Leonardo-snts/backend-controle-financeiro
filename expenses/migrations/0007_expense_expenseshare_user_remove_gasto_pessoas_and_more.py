# Generated by Django 5.1.3 on 2024-12-04 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_gasto_gastopessoa_gasto_pessoas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('installment', models.IntegerField(default=1)),
                ('total_installments', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expense')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='pessoas',
        ),
        migrations.RemoveField(
            model_name='gastopessoa',
            name='gasto',
        ),
        migrations.RemoveField(
            model_name='gastopessoa',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='UploadArquivo',
        ),
        migrations.AddField(
            model_name='expenseshare',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.user'),
        ),
        migrations.AddField(
            model_name='expense',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_expenses', through='expenses.ExpenseShare', to='expenses.user'),
        ),
        migrations.DeleteModel(
            name='Gasto',
        ),
        migrations.DeleteModel(
            name='GastoPessoa',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
