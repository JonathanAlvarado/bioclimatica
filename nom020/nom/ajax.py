from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from nom.models import estados, ciudades, soluciones, soluciones_detalles, ciudades_k, ciudades_fg, ciudades_temp
from django.db.models import Q

@dajaxice_register
def multiply(request, a, b):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result','value',str(result))
	return dajax.json()

@dajaxice_register
def get_states(request):
	dajax = Dajax()
	states = [['','Escoge un estado']]
	states = [['', 'Escoge un estado'], ] + [ [state.id, state.estado] for state in estados.objects.all() ]
	
	options = []

	for state in states:
		options.append( "<option value='%s'>%s</option>" % ( state[0], state[1]) )

	dajax.assign( '#estados', 'innerHTML', ''.join( options ) )
	return dajax.json()


@dajaxice_register
def update_city(request, option):
	dajax = Dajax()
	cities = [['','Escoge una ciudad']]
	
	for city in ciudades.objects.all():
		if city.estado_id == int(option):
			cities.append([city.id, city.ciudad])
	
	options = []
	
	for city in cities:
		options.append( "<option value='%s'>%s</option>" % ( city[0], city[1]) )

	dajax.assign( '#ciudades', 'innerHTML', ''.join( options ) )
	return dajax.json()

