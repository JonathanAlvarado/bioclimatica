from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from nom.models import ciudades

@dajaxice_register(name='nom.update_city')
def update_city(request, option):
	dajax = Dajax()
	cities = [['','Escoge una ciudad']]
	for city in ciudades.objects.all():
		if city.estado_id == int(option):
			cities.append([city.id, city.ciudad])

	options = []
	for city in cities:
		options.append( "<option value='%s'>%s</option>" % ( city[0], city[1]) )

	dajax.assign( '#id_ciudad', 'innerHTML', ''.join( options ) )
	return dajax.json()