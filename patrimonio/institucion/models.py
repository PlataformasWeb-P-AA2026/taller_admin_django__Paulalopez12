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
    idiomas_hablados = models.CharField(max_length=100)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='guias')

    def __str__(self):
        return self.nombre_completo

class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name='exhibiciones')
