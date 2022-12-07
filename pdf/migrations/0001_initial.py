# Generated by Django 4.0.3 on 2022-12-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_addr', models.CharField(max_length=100)),
                ('your_name', models.CharField(max_length=100)),
                ('your_addr', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('campus_name', models.CharField(max_length=100)),
                ('skill', models.TextField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),                
            ],
        ),
    ]
