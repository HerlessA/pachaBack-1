# Generated by Django 4.2.3 on 2023-07-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='fechaTakeoff',
            field=models.DateField(),
        ),
    ]
