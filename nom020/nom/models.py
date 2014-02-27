from django.db import models
'''
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'wazon'): 
Email address: jonathan.aam92@gmail.com    
Password: 
'''
# Create your models here.
class ciudades(models.Model):
	ciudad = models.CharField(max_length=30)
	estado = models.CharField(max_length=30)

class ciudades_fg(models.Model):
	ciudad = models.ForeignKey(ciudades)
	fgtd = models.IntegerField(default=0)
	fg_mN = models.IntegerField(default=0)
	fg_mE = models.IntegerField(default=0)
	fg_mO = models.IntegerField(default=0)
	fg_mS = models.IntegerField(default=0)

class ciudades_k(models.Model):
	ciudad = models.ForeignKey(ciudades)
	kref_3niv = models.FloatField(default=0.0)
	kref_mas3niv_techo = models.FloatField(default=0.0)
	kref_mas3niv_pared = models.FloatField(default=0.0)

class ciudades_temp(models.Model):
	ciudad = models.ForeignKey(ciudades)
	temp_int = models.IntegerField(default=0)
	temp_sup_int = models.IntegerField(default=0)
	temp_techo = models.IntegerField(default=0)
	temp_mmN = models.IntegerField(default=0)
	temp_mmE = models.IntegerField(default=0)
	temp_mmO = models.IntegerField(default=0)
	temp_mmS = models.IntegerField(default=0)
	temp_mlN = models.IntegerField(default=0)
	temp_mlE = models.IntegerField(default=0)
	temp_mlO = models.IntegerField(default=0)
	temp_mlS = models.IntegerField(default=0)
	temp_trluz_domo = models.IntegerField(default=0)
	temp_ventN = models.IntegerField(default=0)
	temp_ventE = models.IntegerField(default=0)
	temp_ventO = models.IntegerField(default=0)
	temp_ventS = models.IntegerField(default=0)

class soluciones(models.Model):
	nombre = models.CharField(max_length=30)

class soluciones_details(models.Model):
	solution = models.ForeignKey(soluciones)
	valueR  = models.FloatField(default=0.0)
	tipo = models.CharField(max_length=30)
	tipo_porcion = models.CharField(max_length=30)
	se = models.FloatField(default=0.0)
	coeficiente_sombreado = models.FloatField(default=0.0)