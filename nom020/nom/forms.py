#-*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from nom.models import soluciones, estados, ciudades

class data_form(forms.Form):
	state_choices = [ ('0', 'Escoge un estado'), ] + [(edo.id, edo.estado) for edo in estados.objects.all()]
	city_choices = [ ('0', 'Escoge una ciudad') ]
	#techo_choices = [('', 'Escoge un material'), ] + [(sol.id, sol.nombre) for sol in soluciones.objects.filter(tipo="techo")]
	#muro_choices = [('', 'Escoge un material'), ] + [(sol.id, sol.nombre) for sol in soluciones.objects.filter( Q(tipo="muro") | Q(tipo="ventana") | Q(tipo="piso") )]
	nfloor_choices = ( 
		('0', 'Pisos de la construcción'), ('1', '1 a 3 pisos'),
    	('4', 'Más de 3 pisos'),
    )
	house_part_choices = [ ('0', 'Parte de la casa') ,('techo', 'Techo'), 
		('ventana', 'Ventana'), ('piso', 'Piso'), ('pared', 'Pared'),
    ]
	ubication_choices = [ ('0', 'Escoge...') ]
	material_choices = [ ('0', 'Escoge un material') ]

	state = forms.ChoiceField( choices = state_choices, label = 'Estado' )
	city = forms.ChoiceField( choices = city_choices, label = 'Ciudad' )
	nfloor = forms.ChoiceField( choices = nfloor_choices, label  = 'Total de pisos' )
	house_part = forms.ChoiceField( choices = house_part_choices, label = 'Parte de la casa' )
	ubication = forms.ChoiceField( choices = ubication_choices, label = 'Ubicación' )
	material = forms.ChoiceField( choices = material_choices, label = 'Material' )
	area = forms.FloatField(label = "Área", max_value = 9000)

'''
	#solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
	#email = forms.EmailField(required=False)
	#message = forms.CharField()'''
