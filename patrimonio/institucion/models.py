from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cuidad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    def obtener_costo_total_exibiciones(self):
        total = sum(exhibicion.costo_produccion 
                    for exhibicion in self.exhibiciones.all())
        return total
    
    def obtener_guia_mas_experiencia(self):
        guia = self.guias.order_by('-anios_experiencia_guia').first()
        return guia.nombre_completo if guia else "No hay guías disponibles"

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
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='exhibiciones')

    def __str__(self):
        return self.titulo_exhibicion