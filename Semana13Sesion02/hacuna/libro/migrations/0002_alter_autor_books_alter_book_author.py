# Generated by Django 4.2.2 on 2023-07-03 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='books',
            field=models.ManyToManyField(null=True, to='libro.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(null=True, to='libro.autor'),
        ),
    ]
