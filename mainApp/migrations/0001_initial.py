# Generated by Django 4.1.2 on 2023-02-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=30)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pdesc', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pdesc', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('password', models.IntegerField()),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
