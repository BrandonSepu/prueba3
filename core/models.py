
from django.db import models



class Alertas(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)



class Configuracion(models.Model):
    id_configuracion = models.IntegerField(primary_key=True)
    recibir_alertas = models.CharField(max_length=1)
    alerta_roja = models.CharField(max_length=1)
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id_usuario')



class Contactos(models.Model):
    id_contacto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=1)
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id_usuario')

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=20)
    telefono = models.IntegerField()
    contrase = models.CharField(max_length=15)

class Denuncia(models.Model):
    id_denucia = models.IntegerField(primary_key=True)
    detalles = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField()
    punto_id_punto = models.ForeignKey('Punto', on_delete=models.CASCADE, db_column='punto_id_punto')
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id_usuario')
    alertas_id_tipo = models.ForeignKey(Alertas, on_delete=models.CASCADE, db_column='alertas_id_tipo')




class Punto(models.Model):
    id_punto = models.IntegerField(primary_key=True)
    longitud = models.DecimalField(max_digits=30, decimal_places=30)
    latitud = models.DecimalField(max_digits=30, decimal_places=30)

