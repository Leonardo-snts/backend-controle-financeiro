# Generated by Django 5.1.3 on 2024-12-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_gasto_pessoa_uploadarquivo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assets/csv/')),
                ('file_type', models.CharField(choices=[('xlsx', 'Excel (.xlsx)'), ('csv', 'CSV (.csv)'), ('pdf', 'PDF (.pdf)')], max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
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
