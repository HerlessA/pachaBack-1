# Generated by Django 4.2.1 on 2023-05-25 21:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lista', models.BinaryField()),
                ('nombre', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('sexo', models.BooleanField()),
                ('gmail', models.EmailField(max_length=254)),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.new')),
            ],
        ),
    ]