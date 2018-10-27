from django.db import models


# Create your models here.

class Raza(models.Model):
    Denominacion = models.CharField(max_length = 100)

    def __str__(self):
        return self.Denominacion


class Estado(models.Model):
    estado = models.CharField(max_length = 40)


    def __str__(self):
        return self.estado

class Mascota(models.Model):
    nombre = models.CharField(max_length =50)
    genero = models.CharField(max_length = 1)
    fechaIngreso = models.DateField
    fechaNacimiento =models.DateField
    descripcion = models.CharField(max_length = 100)
    imagen= models.CharField(max_length = 10)
    raza = models.ForeignKey(Raza, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)


    def __str__(self):
        return self.nombre


class Region(models.Model):
    Nregion = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.Nregion

    class Meta:
        verbose_name="Region"        
        verbose_name_plural="Regiones"   


class Ciudad(models.Model):
    Nciudad = models.CharField(max_length = 200)

    def __str__(self):
            return self.Nciudad
    class Meta:
            verbose_name="Ciudad"    
            verbose_name_plural="Cuidades" 

class Comuna(models.Model):
    Ncomuna=models.CharField(max_length=50)
     
     
    def __str__(self):
            return self.Ncomuna

    class Meta:
            verbose_name="Comuna"    
            verbose_name_plural="Comunas" 
    

class TipoVivienda(models.Model):
    
    dtipoVivienda = models.CharField(max_length = 200)
    
    



class Postulante(models.Model):
    rut = models.CharField(max_length=10)
    nombreP = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField()
    email = models.EmailField()
    numeroContacto = models.IntegerField()
    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    tipovivienda = models.ForeignKey(TipoVivienda, on_delete = models.CASCADE)

