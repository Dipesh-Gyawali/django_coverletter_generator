# Generated by Django 4.0.3 on 2022-12-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]