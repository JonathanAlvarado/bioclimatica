from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from nom.models import estados, ciudades, soluciones, soluciones_detalles, ciudades_k, ciudades_fg, ciudades_temp
from django.db.models import Q

'''@dajaxice_register
def multiply( request, a, b ):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result','value',str(result))
	return dajax.json()'''


@dajaxice_register
def get_states( request ):
	dajax = Dajax()
	states = [[ '','Escoge un estado' ]]
	states = [ [ '', 'Escoge un estado' ], ] + [ [ state.id, state.estado ] for state in estados.objects.all() ]
	
	options = []

	for state in states:
		options.append( "<option value='%s'>%s</option>" % ( state[0], state[1]) )

	dajax.assign( '#states', 'innerHTML', ''.join( options ) )
	return dajax.json()


@dajaxice_register
def update_city( request, option ):
	dajax = Dajax()
	cities = [[ '','Escoge una ciudad' ]]
	
	request.session['state'] = int(option)

	for city in ciudades.objects.all():
		if city.estado_id == int(option):
			cities.append([ city.id, city.ciudad ])
	
	options = []
	
	for city in cities:
		options.append( "<option value='%s'>%s</option>" % ( city[0], city[1]) )

	dajax.assign( '#cities', 'innerHTML', ''.join( options ) )
	return dajax.json()


@dajaxice_register
def get_materials( request, house_part ):
	dajax = Dajax()

	wall_options  = [ "<option value='0'>Escoge un material</option>" ]
	floor_options = [ "<option value='0'>Escoge un material</option>" ]
	roof_options = [ "<option value='0'>Escoge un material</option>" ]
	window_options = [ "<option value='0'>Escoge un material</option>" ]

	for sol in soluciones.objects.all():
		if sol.tipo == "muro":
			wall_options.append( "<option value='%s'>%s</option>" % ( sol.id, sol.nombre) )
		elif sol.tipo == "piso":
			floor_options.append( "<option value='%s'>%s</option>" % ( sol.id, sol.nombre) )
		elif sol.tipo == "techo":
			roof_options.append( "<option value='%s'>%s</option>" % ( sol.id, sol.nombre) )
		elif sol.tipo == "ventana":
			window_options.append( "<option value='%s'>%s</option>" % ( sol.id, sol.nombre) )

	if ( house_part == 'muro' ):
		dajax.assign( '#material', 'innerHTML', ''.join( wall_options ) )
	elif ( house_part == 'techo' ):
		dajax.assign( '#material', 'innerHTML', ''.join( roof_options ) )
	elif ( house_part == 'ventana' ):
		dajax.assign( '#material', 'innerHTML', ''.join( window_options ) )
	elif ( house_part == 'piso' ):
		dajax.assign( '#material', 'innerHTML', ''.join( floor_options ) )

	return dajax.json()


@dajaxice_register
def submit_material( request, h_part, ubication, material, area ):
	dajax = Dajax()
	user_materials = [ h_part, ubication, material, area ]
	materials =	[]
	options = []
	
	if request.session.get( 'materials' ):
		materials = request.session.pop( 'materials' )
		
	materials.append( user_materials )
	request.session['materials'] = materials

	for mat in materials:
		nom_mat = soluciones.objects.get( id= int( mat[2] ) )
		options.append( "<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ( mat[0], mat[1], nom_mat.nombre, mat[3] ) )

	#dajax.add_data( data, callback_function)
	dajax.add_data( options , 'ajax_table')
	return dajax.json()


@dajaxice_register
def calculate(request, city):
	dajax = Dajax()
	request.session['materials'] = int(city)
