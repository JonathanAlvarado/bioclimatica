from django import forms
from nom.models import soluciones, estados, ciudades

class cityForm(forms.Form):
	state_choices = [('', 'Escoge un estado'), ] + [(edo.id, edo.estado) for edo in estados.objects.all()]
	solutions_choices = [('', 'Escoge un material'), ] + [(sol.id, sol.nombre) for sol in soluciones.objects.all()]
	estado = forms.ChoiceField( choices = state_choices )
	ciudad = forms.ChoiceField([('0','Escoge una ciudad')])
	muroNorte = forms.ChoiceField( choices = solutions_choices, label = "Material Muro Norte" )
	areaN = forms.CharField(label = "Área Muro Norte")
	muroSur = forms.ChoiceField( choices = solutions_choices, label = "Material Muro Sur" )
	areaS = forms.CharField(label = "Área Muro Sur")
	muroEste = forms.ChoiceField( choices = solutions_choices, label = "Material Muro Este" )
	areaE = forms.CharField(label = "Área Muro Este")
	muroOeste = forms.ChoiceField( choices = solutions_choices, label = "Material Muro Oeste" )
	areaO = forms.CharField(label = "Área Muro Oeste")

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

	estado = forms.ChoiceField( choices = estados )
	ciudad = forms.ChoiceField( choices = ciudades )
	pisos = forms.CharField()
	muroNorte = forms.ChoiceField( choices = soluciones, label = "Material Muro Norte" )
	areaN = forms.CharField(label = "Area Muro Norte")
	muroSur = forms.ChoiceField( choices = soluciones, label = "Material Muro Sur" )
	areaS = forms.CharField(label = "Area Muro Sur")
	muroEste = forms.ChoiceField( choices = soluciones, label = "Material Muro Este" )
	areaE = forms.CharField(label = "Area Muro Este")
	muroOeste = forms.ChoiceField( choices = soluciones, label = "Material Muro Oeste" )
	areaO = forms.CharField(label = "Area Muro Oeste")
	#solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
	#email = forms.EmailField(required=False)
	#message = forms.CharField()'''