from django import forms

class ContactForm(forms.Form):
	estados = ( 
		('Zacatecas', 'Zacatecas'),
    	('Veracruz', 'Veracruz'),
    )

	ciudades = (
    	('Fresnillo','Fresnillo'),
    	('Jalapa', 'Jalapa'),
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
	#message = forms.CharField()