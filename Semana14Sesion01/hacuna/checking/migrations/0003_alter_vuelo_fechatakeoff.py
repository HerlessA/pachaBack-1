# Generated by Django 4.2.3 on 2023-07-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checking', '0002_alter_vuelo_fechatakeoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='fechaTakeoff',
            field=models.DateTimeField(),
        ),
    ]
