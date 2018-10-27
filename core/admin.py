from django.contrib import admin
from .models import *
#from .models import Region,Ciudad,TipoVivienda,Postulante

# Register your models here.



class MisPerrisAdmin(admin.ModelAdmin):
    list_display=('nombre','raza','estado')



class PostulanteAdmin(admin.ModelAdmin):
    list_display=('rut', 'region','ciudad','comuna','tipovivienda')







admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Mascota, MisPerrisAdmin)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(TipoVivienda)
admin.site.register(Raza)
admin.site.register(Estado)


