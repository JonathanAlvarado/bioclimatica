from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from nom.models import estados, ciudades, soluciones, soluciones_detalles, ciudades_k, ciudades_fg, ciudades_temp, results
import simplejson as json
#from django.db.models import Q

'''@dajaxice_register
def multiply( request, a, b ):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result','value',str(result))
	return dajax.json()'''


@dajaxice_register
def get_states( request ):
	dajax = Dajax()
	#states = [[ '','Escoge un estado' ]]
	states = [ [ '', 'Escoge un estado' ], ] + [ [ state.id, state.estado ] for state in estados.objects.all() ]
	
	options = []

	for state in states:
		options.append( "<option value='%s'>%s</option>" % ( state[0], state[1]) )

	dajax.assign( '#states', 'innerHTML', ''.join( options ) )
	return dajax.json()


@dajaxice_register
def update_city( request, option ):
	dajax = Dajax()
	cities = [[ '0','Escoge una ciudad' ]]
	
	request.session['state'] = int(option)

	for city in ciudades.objects.all():
		if city.estado_id == int(option):
			cities.append([ city.id, city.ciudad ])
	
	options = []
	
	for city in cities:
		options.append( "<option value='%s'>%s</option>" % ( city[0], city[1]) )

	dajax.assign( '#cities', 'innerHTML', ''.join( options ) )
	#dajax.assign( '#id_city', 'innerHTML', ''.join( options ) )
	return dajax.json()


@dajaxice_register
def get_ubication( request, hpart):
	dajax = Dajax()
	ubications = ( ['0', 'Escoge...'], [ 'norte','Pared norte' ], 
		[ 'sur','Pared sur' ], [ 'este','Pared este' ], 
		[ 'oeste','Pared oeste' ] 
	)
	options = []

	if ( hpart == 'techo' ):
		options.append( "<option value='%s'>%s</option>" % ( '0' , 'Escoge...' ) )
		options.append( "<option value='%s'>%s</option>" % ( 'techo' , 'Techo' ) )

	elif ( hpart == 'ventana') or (hpart == 'pared' ):
		for ub in ubications:
			options.append( "<option value='%s'>%s</option>" % ( ub[0], ub[1]) )

	elif ( hpart == 'piso' ):
		options.append( "<option value='%s'>%s</option>" % ( '0' , 'Escoge...' ) )
		options.append( "<option value='%s'>%s</option>" % ( 'piso' , 'Piso' ) )

	dajax.assign( '#ubication', 'innerHTML', ''.join( options ) )
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
	
	materials.append( user_materials )
	request.session['materials'] = materials

	for mat in materials:
		nom_mat = soluciones.objects.get( id= int( mat[2] ) )
		options.append( "<tr><th>%s</th><th>%s</th><th>%s</th><th>%s m.</th></tr>" % ( mat[0], mat[1], nom_mat.nombre, mat[3] ) )

	#dajax.add_data( data, callback_function)
	dajax.add_data( options , 'ajax_table')
	return dajax.json()

def get_k(city, floors):
	k_city = ciudades_k.objects.get( ciudad_id = city )

	if(floors <= 3):
		k_roof = k_city.kref_3niv
		k_wall = k_city.kref_3niv

	elif(floors > 3):
		k_roof = k_city.kref_mas3niv_techo
		k_wall = k_city.kref_mas3niv_pared

	return k_roof,k_wall


def check_orientations():
	materials = request.session.get( 'materials' )
	orientations = ['norte','sur','este','oeste']

	for o in orientations:
		if any( i in x for x in a ) == False:
			return False
			break
	return True

@dajaxice_register
def calculate( request, city, floors):
	# pandas http://www.dyinglovegrape.com/data_analysis/part1/1da3.php
	# pandas http://bconnelly.net/2013/10/summarizing-data-in-python-with-pandas/

	if check_orientations() == True:
		dajax = Dajax()
		state = request.session.get( 'state' )
		materials = request.session.get( 'materials' )

		city = int(city)
		floors = int(floors)
		request.session['city'] = city
		request.session['floors'] = floors

		fcRef = 0.1
		cgsRef = 1
		kGlobalV = 5.319
		areaTecho = areaMN = areaMS = areaME = areaMO = areaPV = 0
		ganCalTechoProy = 0
		ganRadVentTechoProy = ganRadVentNProy = ganRadVentSProy = ganRadVentEProy = ganRadVentOProy = ganCalTechoRef = 0
		coConduc = 0
		ganCalMNProy = ganCalMNRef = ganCalMEProy = ganCalMERef = ganCalMSProy = ganCalMSRef = ganCalMOProy = ganCalMPisoProy = ganCalMORef = 0
		ganRadVentTechoRef = ganRadVentNRef = ganRadVentERef = ganRadVentSRef = ganRadVentORef = 0

		k = get_k( city, floors )
		city_details = ciudades_temp.objects.get( ciudad_id = city )
		city_fg = ciudades_fg.objects.get( ciudad_id = city )

		for mat in materials:
			if mat[1] == 'techo':
				areaTecho += int( mat[3] )
			elif mat[1] == 'norte':
				areaMN += int( mat[3] )
			elif mat[1] == 'sur':
				areaMS += int( mat[3] )
			elif mat[1] == 'este':
				areaME += int( mat[3] )
			elif mat[1] == 'oeste':
				areaMO += int( mat[3] )
			elif mat[1] == 'piso':
				areaPV += int( mat[3] )
	
	#solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
		for i in xrange( len(materials) ):
			mat_details = soluciones_detalles.objects.get( solucion_id = materials[i][2] )
		
			if materials[i][1] == "techo": #ubication -> techo
				if mat_details.tipo_porcion == "superficie inferior":
					ganCalTechoProy += ( ( 1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_sup_int - city_details.temp_int ) )
				elif mat_details.tipo_porcion == "techo":
					ganCalTechoProy += ( ( 1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_techo - city_details.temp_int ) )
				elif mat_details.tipo_porcion == "domo":
					ganCalTechoProy += ( ( 1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_trluz_domo - city_details.temp_int ) )

					ganRadVentTechoProy += ( mat_details.coeficiente_sombreado * int( materials[i][3] ) * city_fg.fgtd - mat_details.se )

			elif materials[i][1] == "norte":
				if mat_details.tipo_porcion == "ventana":
					ganCalMNProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_ventN - city_details.temp_int ) )

					ganRadVentNProy += ( mat_details.coeficiente_sombreado * int( materials[i][3] ) * city_fg.fg_mN * mat_details.se )
				elif mat_details.tipo_porcion == "muro masivo":
					ganCalMNProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mmN - city_details.temp_int ) )

				elif mat_details.tipo_porcion == "muro ligero":
					ganCalMNProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mlN - city_details.temp_int ) )

			elif materials[i][1] == "este":
				if mat_details.tipo_porcion == "ventana":
					ganCalMEProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_ventE - city_details.temp_int ) )

					ganRadVentEProy += ( mat_details.coeficiente_sombreado * int( materials[i][3] ) * city_fg.fg_mE * mat_details.se )
            
				elif mat_details.tipo_porcion == "muro masivo":
					ganCalMEProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mmE - city_details.temp_int ) )

				elif mat_details.tipo_porcion == "muro ligero":
					ganCalMEProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mlE - city_details.temp_int ) )

			elif materials[i][1] == "sur":
				if mat_details.tipo_porcion == "ventana":
					ganCalMSProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_ventS - city_details.temp_int ) )

					ganRadVentSProy += ( mat_details.coeficiente_sombreado * int( materials[i][3] ) * city_fg.fg_mS * mat_details.se )

				elif mat_details.tipo_porcion == "muro masivo":
					ganCalMSProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mmS - city_details.temp_int ) )

				elif mat_details.tipo_porcion == "muro ligero":
					ganCalMSProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mlS - city_details.temp_int ) )

			elif materials[i][1] == "oeste":
				if mat_details.tipo_porcion == "ventana":
					ganCalMOProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_ventO - city_details.temp_int ) )

					ganRadVentOProy += ( mat_details.coeficiente_sombreado * int( materials[i][3] ) * city_fg.fg_mO * mat_details.se )

				elif mat_details.tipo_porcion == "muro masivo":
					ganCalMOProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mmO - city_details.temp_int ) )

				elif mat_details.tipo_porcion == "muro ligero":
					ganCalMOProy += ( (1 / mat_details.valorR ) * int( materials[i][3] ) * ( city_details.temp_mlO - city_details.temp_int ) )


		ganRadVentTechoRef += ( cgsRef * areaTecho * (0) * city_fg.fgtd )
		ganCalTechoRef += ( k[0] * areaTecho * ( 1 - (0) ) * ( city_details.temp_techo - city_details.temp_int ) )
		coConducTecho = ganCalTechoProy - ganCalTechoRef

		ganRadVentNRef += ( cgsRef * areaMN * ( fcRef ) * city_fg.fg_mN )
		ganCalMNRef += ( k[1] * areaMN * (1 - ( fcRef )) * ( city_details.temp_mmN - city_details.temp_int ) )
		ganCalVentNRef = k[0] * areaMN * (fcRef) * ( city_details.temp_ventN - city_details.temp_int )
		coConducMN = ganCalMNProy - ganCalMNRef

		ganRadVentERef += ( cgsRef * areaME * ( fcRef ) * city_fg.fg_mE )
		ganCalMERef += ( k[1] * areaME * (1 - ( fcRef ) ) * ( city_details.temp_mmE - city_details.temp_int ) )
		ganCalVentERef = k[0] * areaME * ( fcRef ) * (city_details.temp_ventE - city_details.temp_int )

		ganRadVentSRef += ( cgsRef * areaMS * ( fcRef ) * city_fg.fg_mS )
		ganCalMSRef += ( k[1] * areaMS * (1 - ( fcRef ) ) * ( city_details.temp_mmS - city_details.temp_int ) )
		ganCalVentSRef = k[0] * areaMS * ( fcRef ) * ( city_details.temp_ventS - city_details.temp_int )

		ganRadVentORef += ( cgsRef * areaMO * ( fcRef ) * city_fg.fg_mO );
		ganCalMORef += ( k[1] * areaMO * (1 - ( fcRef ) ) * ( city_details.temp_mmO - city_details.temp_int ) )
		ganCalVentORef = k[0] * areaMO * ( fcRef ) * ( city_details.temp_ventO - city_details.temp_int )

		ganRadTotRef = ganRadVentNRef + ganRadVentERef + ganRadVentORef + ganRadVentSRef + ganRadVentTechoRef
		ganRadTotProy = ganRadVentNProy + ganRadVentEProy + ganRadVentOProy + ganRadVentSProy + ganRadVentTechoProy

		ganCalTotMuroRef = ganCalMNRef + ganCalMERef + ganCalMORef + ganCalMSRef + ganCalTechoRef + ganCalVentNRef + ganCalVentERef + ganCalVentORef + ganCalVentSRef
		ganCalTotMuroProy = ganCalMNProy + ganCalMEProy + ganCalMOProy + ganCalMSProy + ganCalTechoProy

		ganCalTotCondProy = ganCalTotMuroProy

		ganCalTotMuroRef = ganCalTotMuroRef + ganRadTotRef
		ganCalTotMuroProy = ganCalTotMuroProy + ganRadTotProy

		ganCalPorcentaje = ( ganCalTotMuroRef - ganCalTotMuroProy) / (ganCalTotMuroRef * -1)

		request.session['nom'] = ganCalPorcentaje * 100
		dajax.add_data( ganCalPorcentaje * 100 , 'result')
		
	else:
		dajax.add_css_class('p .error', 'red')

	return dajax.json()

def insert_data( result ):
	state = request.session.get( 'state' )
	city = request.session.get( 'city' )
	nfloors = request.session.get( 'floors' )
	materials = json.dumps( request.session.get( 'materials' ) )

	data = results( estado=state, ciudad=city, pisos=nfloors, materiales=materials, nom=result )
	data.save()