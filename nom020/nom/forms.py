#-*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from nom.models import soluciones, estados, ciudades

class cityForm(forms.Form):
	estado_choices = [('', 'Escoge un estado'), ] + [(edo.id, edo.estado) for edo in estados.objects.all()]
	techo_choices = [('', 'Escoge un material'), ] + [(sol.id, sol.nombre) for sol in soluciones.objects.filter(tipo="techo")]
	muro_choices = [('', 'Escoge un material'), ] + [(sol.id, sol.nombre) for sol in soluciones.objects.filter( Q(tipo="muro") | Q(tipo="ventana") | Q(tipo="piso") )]
	pisos_choices = ( 
		('0', 'Pisos de la construcción'),
    	('1', '1 a 3 pisos'),
    	('2', 'Más de 3 pisos'),
    )
	
	estado = forms.ChoiceField( choices = estado_choices )
	ciudad = forms.ChoiceField([('0','Escoge una ciudad')])
	pisos = forms.ChoiceField( choices = pisos_choices, label  = "Total de pisos" )
	
	techo = forms.ChoiceField( choices = techo_choices, label = "Material techo" )
	areaT = forms.CharField(label = "Área muro norte")
	
	muroNorte = forms.ChoiceField( choices = muro_choices, label = "Material muro norte" )
	areaN = forms.CharField(label = "Área muro norte")
	
	muroSur = forms.ChoiceField( choices = muro_choices, label = "Material muro sur" )
	areaS = forms.CharField(label = "Área muro sur")
	
	muroEste = forms.ChoiceField( choices = muro_choices, label = "Material muro este" )
	areaE = forms.CharField(label = "Área muro este")
	
	muroOeste = forms.ChoiceField( choices = muro_choices, label = "Material muro oeste" )
	areaO = forms.CharField(label = "Área muro oeste")

'''
class ContactForm(forms.Form):
	estados = ( 
		edos = ciudades.objects.values('estado').distinct()
    )

	ciudades = (
    	('Fresnillo','Fresnillo'),
    )

	soluciones = (
    	('Ejemplo Muro','Ejemplo Muro'),
    	('Ejemplo Losa', 'Ejemplo Losa'),
    )

	#solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
	#email = forms.EmailField(required=False)
	#message = forms.CharField()'''
