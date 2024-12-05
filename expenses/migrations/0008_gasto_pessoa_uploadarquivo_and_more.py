# Generated by Django 5.1.3 on 2024-12-04 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_expense_expenseshare_user_remove_gasto_pessoas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parcela', models.CharField(blank=True, max_length=20, null=True)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadArquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='assets/csv/')),
                ('upload_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='expenseshare',
            name='expense',
        ),
        migrations.RemoveField(
            model_name='expenseshare',
            name='user',
        ),
        migrations.CreateModel(
            name='GastoPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gasto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.gasto')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='gasto',
            name='pessoas',
            field=models.ManyToManyField(through='expenses.GastoPessoa', to='expenses.pessoa'),
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='ExpenseShare',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]