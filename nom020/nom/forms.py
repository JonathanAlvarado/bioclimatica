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
	areaT = forms.FloatField(label = "Área techo", max_value = 9000)
	
	muroNorte = forms.ChoiceField( choices = muro_choices, label = "Material muro norte" )
	areaN = forms.FloatField(label = "Área muro norte", max_value = 9000)
	
	muroSur = forms.ChoiceField( choices = muro_choices, label = "Material muro sur" )
	areaS = forms.FloatField(label = "Área muro sur", max_value = 9000)
	
	muroEste = forms.ChoiceField( choices = muro_choices, label = "Material muro este" )
	areaE = forms.FloatField(label = "Área muro este", max_value = 9000)
	
	muroOeste = forms.ChoiceField( choices = muro_choices, label = "Material muro oeste" )
	areaO = forms.FloatField(label = "Área muro oeste", max_value = 9000)

'''
	#solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
	#email = forms.EmailField(required=False)
	#message = forms.CharField()'''
