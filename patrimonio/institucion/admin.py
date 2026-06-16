from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuidad', 'anio_fundacion', 'obtener_costo_total_exibiciones', 'obtener_guia_mas_experiencia')

class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')

class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'guia')

admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo, GuiaMuseoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)