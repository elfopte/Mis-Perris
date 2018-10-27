from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def galeria(request):
        return render(request,'core/galeria.html')

def registroPostulante(request):
        regiones=Region.objects.all()
        ciudades=Ciudad.objects.all()
        comuna=Comuna.objects.all()
        viviendas=TipoVivienda.objects.all()
        variables={
                'regiones':regiones,
                'ciudades':ciudades,
                'comuna':comuna,
                'viviendas':viviendas
    }

        if request.POST:
            postulante =Postulante()
            postulante.rut = request.POST.get('txtRut')
            postulante.nombreP = request.POST.get('txtNombreCompleto')
            postulante.fechaNacimiento = request.POST.get('dtpFechaNacimiento')
            postulante.email = request.POST.get('txtEmail')
            postulante.numeroContacto = request.POST.get('txtTelefono')

            region = Region()
            region.id = str(request.POST.get('cboRegion'))
            postulante.region = region

            ciudad = Ciudad()
            ciudad.id = str(request.POST.get('cboCiudad'))
            postulante.ciudad = ciudad

            comuna = Comuna()
            comuna.id = str(request.POST.get('cboComuna'))
            postulante.comuna = comuna

            tvivienda = TipoVivienda()
            tvivienda.id = str(request.POST.get('cboTipoVivivenda'))
            postulante.tvivienda = tvivienda

            try:
                postulante.save()
                variables['mensaje'] ="Guardado pulentoso"
            except:
                variables['mensaje'] = "No se ha Guardado"
            
        return render(request, 'core/registroPostulante.html', variables)


#crud regsitrar mascota
#def registroMascota(request):
#        mascota = Mascota.objects.all()
#        
#
#        return render(request,'core/registroMascota.html', mascota,{
#
#                'mascota':mascota
#        })