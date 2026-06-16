from django.db import models

# Creamos las clases 
class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cuidad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=100)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.Fore
    

