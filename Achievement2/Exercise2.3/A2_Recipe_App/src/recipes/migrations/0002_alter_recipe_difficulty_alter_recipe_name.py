# Generated by Django 4.2.17 on 2024-12-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
