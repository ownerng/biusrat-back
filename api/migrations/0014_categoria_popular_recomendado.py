# Generated by Django 5.0.6 on 2024-05-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_todaymeal_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('b_image', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('kcal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recomendado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('kcal', models.CharField(max_length=50)),
            ],
        ),
    ]
