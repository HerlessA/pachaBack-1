# Generated by Django 4.2.3 on 2023-07-03 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('columna', models.CharField(max_length=2)),
                ('fila', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipoasiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaTakeoff', models.DateField(auto_now=True)),
                ('aeropuertoTakeOff', models.CharField(max_length=200)),
                ('fechaLanding', models.DateTimeField()),
                ('aeropuertoLanding', models.CharField(max_length=200)),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.avion')),
            ],
        ),
        migrations.CreateModel(
            name='BoardingPass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.asiento')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.compra')),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.pasajero')),
                ('tipoAsiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.tipoasiento')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.vuelo')),
            ],
        ),
        migrations.AddField(
            model_name='asiento',
            name='avion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.avion'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='tipoAsiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checking.tipoasiento'),
        ),
    ]