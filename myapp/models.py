from django.db import models

class tb_proceso_electoral (models.Model):
    name = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)

class tb_candidaturas(models.Model):
    nombre = models.CharField(max_length= 50)

class tb_listas(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    cod_color = models.CharField(max_length=10)
    slogan = models.CharField(max_length=250)
    estado = models.IntegerField(default=1)

class tb_propuestas(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.IntegerField(default=1)

class tb_lista_propuestas(models.Model):
    lista = models.ForeignKey(tb_listas, on_delete=models.CASCADE)
    propuestas = models.ForeignKey(tb_propuestas, on_delete=models.CASCADE)