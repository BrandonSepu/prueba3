# Generated by Django 3.2.9 on 2022-06-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alertas',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id_punto', models.IntegerField(primary_key=True, serialize=False)),
                ('longitud', models.DecimalField(decimal_places=30, max_digits=30)),
                ('latitud', models.DecimalField(decimal_places=30, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('rut', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('contrase', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id_denucia', models.IntegerField(primary_key=True, serialize=False)),
                ('detalles', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField()),
                ('alertas_id_tipo', models.ForeignKey(db_column='alertas_id_tipo', on_delete=django.db.models.deletion.CASCADE, to='core.alertas')),
                ('punto_id_punto', models.ForeignKey(db_column='punto_id_punto', on_delete=django.db.models.deletion.CASCADE, to='core.punto')),
                ('usuario_id_usuario', models.ForeignKey(db_column='usuario_id_usuario', on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id_contacto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=1)),
                ('usuario_id_usuario', models.ForeignKey(db_column='usuario_id_usuario', on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id_configuracion', models.IntegerField(primary_key=True, serialize=False)),
                ('recibir_alertas', models.CharField(max_length=1)),
                ('alerta_roja', models.CharField(max_length=1)),
                ('usuario_id_usuario', models.ForeignKey(db_column='usuario_id_usuario', on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
