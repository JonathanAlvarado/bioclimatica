from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from nom.models import soluciones, soluciones_detalles, ciudades_k, ciudades_fg, ciudades_temp
from django.db.models import Q

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

@dajaxice_register(name='nom.send_form')
def send_form(request, form):
	dajax = Dajax()
	form = cityForm( deserialize_form( form ) )

	if form.is_valid():
		dajax.remove_css_class('#data_form input', 'error')
		state = int( form.cleaned_data.get('estado') )
		city = int( form.cleaned_data.get('ciudad') )
		floors = int( form.cleaned_data.get('pisos') )
		

		#dajax.alert("Form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
	else:
		dajax.remove_css_class('#data_form input', 'error')
		for error in form.errors:
			dajax.add_css_class('#id_%s' % error, 'error')
	return dajax.json()


def get_k(state, city, floors):
    if(floors == 1):
        data = ciudades_k.objects.get( ciudad_id = city )
        k_roof = data.kref_3niv
        k_wall = data.kref_3niv

    elif(floors == 2):
        data = ciudades_k.objects.get( ciudad_id = city )
        k_roof = data.kref_mas3niv_techo
        k_wall = data.kref_mas3niv_pared

    return k_roof,k_wall


def calculate(state, city, floors, solutions):
    fcRef = 0.1
    cgsRef = 1
    kGlobalV = 5.319
    areaTecho = areaMN = areaMS = areaME = areaMO = areaPV = 0
    ganCalTechoProy=0;
    ganRadVentTechoProy = ganRadVentNProy = ganRadVentSProy = ganRadVentEProy = ganRadVentOProy = ganCalTechoRef = 0
    coConduc = 0
    ganCalMNProy = ganCalMNRef = ganCalMEProy = ganCalMERef = ganCalMSProy = ganCalMSRef = ganCalMOProy = ganCalMPisoProy = ganCalMORef = 0
    ganRadVentTechoRef = ganRadVentNRef = ganRadVentERef = ganRadVentSRef = ganRadVentORef = 0

    k = get_k(state, city, floors)

    for i in solutions:
        if solutions[1][0] == 'techo':
            areaTecho += solutions[1][2]
        elif solutions[1][0] == 'muroNorte':
            areaMN += solutions[1][2]
        elif solutions[1][0] == 'muroSur':
            areaMS += solutions[1][2]
        elif solutions[1][0] == 'muroEste':
            areaME += solutions[1][2]
        elif solutions[1][0] == 'muroOeste':
            areaMO += solutions[1][2]
        elif solutions[1][0] == 'Piso':
            areaPV += solutions[1][2]

    fg = ciudades_fg.objects.get( ciudad_id = city )
    temp = ciudades_temp.objects.get( ciudad_id = city )
    
    for i in range( len(solutions) ):
        sol_details = soluciones_detalles.objects.get( solucion_id = algo )

        if solutions[i][0] == "techo":
            if solutions[i][1] == "Superficie Inferior":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_sup_int - temp.temp_int ) )
            elif solutions[i][1] == "Techo":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_techo - temp.temp_int ) )
            elif solutions[i][1] == "Domo":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_trluz_domo - temp.temp_int ) )
                
                ganRadVentTechoProy += ( solutions_details[0][6] * solution[i][3] * fg.fgtd - solutions_details[0][5]);

        elif solutions[i][0] == "muroNorte":
            if solutions[i][1] == "Ventana":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_ventN - temp.temp_int ) )
                
                ganRadVentNProy += ( solutions_details[0][6] * solutions[i][2] * fg.fg_mN * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mmN - temp.temp_int ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mlN - temp.temp_int ) )
        
        elif solutions[i][0] == "muroEste":
            if solutions[i][1] == "Ventana":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_ventE - temp.temp_int ) )
                
                ganRadVentEProy += ( solutions_details[0][6] * solutions[i][2] * fg.fg_mE * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mmE - temp.temp_int ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mlO - temp.temp_int ) )

        elif solutions[i][0] == "muroSur":
            if solutions[i][1] == "Ventana":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_ventS - temp.temp_int ) )
                
                ganRadVentSProy += ( solutions_details[0][6] * solutions[i][2] * fg.fg_mS * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mmS - temp.temp_int ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mlS - temp.temp_int ) )
        

        elif solutions[i][0] == "muroOeste":
            if solutions[i][1] == "Ventana":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_ventO - temp.temp_int ) )
                
                ganRadVentEProy += ( solutions_details[0][6] * solutions[i][2] * fg.fg_mO * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mmO - temp.temp_int ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( temp.temp_mlO - temp.temp_int ) )


    ganRadVentTechoRef += ( cgsRef * areaTecho * (0) * fg.fgtd )
    ganCalTechoRef += ( k[0] * areaTecho * ( 1 - (0) ) * ( temp.temp_techo - temp.temp_int ) )
    coConducTecho = ganCalTechoProy - ganCalTechoRef

    ganRadVentNRef += ( cgsRef * areaMN * ( fcRef ) * fg.fg_mN )
    ganCalMNRef += ( k[1] * areaMN * (1 - ( fcRef )) * ( temp.temp_mmN - temp.temp_int ) )
    ganCalVentNRef = k[0] * areaMN * (fcRef) * ( temp.temp_ventN - temp.temp_int )
    coConducMN = ganCalMNProy - ganCalMNRef

    ganRadVentERef += ( cgsRef * areaME * ( fcRef ) * fg.fg_mE );
    ganCalMERef += ( k[1] * areaME * (1 - ( fcRef ) ) * ( temp.temp_mmE - temp.temp_int ) )
    ganCalVentERef = k[0] * areaME * ( fcRef ) * (temp.temp_ventE - temp.temp_int )

    ganRadVentSRef += ( cgsRef * areaMS * ( fcRef ) * fg.fg_mS);
    ganCalMSRef += ( k[1] * areaMS * (1 - ( fcRef ) ) * ( temp.temp_mmS - temp.temp_int ) );
    ganCalVentSRef = k[0] * areaMS * ( fcRef ) * ( temp.temp_ventS - temp.temp_int )

    ganRadVentORef += ( cgsRef * areaMO * ( fcRef ) * fg.fg_mO);
    ganCalMORef += ( k[1] * areaMO * (1 - ( fcRef ) ) * ( temp.temp_mmO - temp.temp_int ) );
    ganCalVentORef = k[0] * areaMO * ( fcRef ) * ( temp.temp_ventO - temp.temp_int )

    ganRadTotRef = ganRadVentNRef + ganRadVentERef + ganRadVentORef + ganRadVentSRef + ganRadVentTechoRef
    ganRadTotProy = ganRadVentNProy + ganRadVentEProy + ganRadVentOProy + ganRadVentSProy + ganRadVentTechoProy

    ganCalTotMuroRef = ganCalMNRef + ganCalMERef + ganCalMORef + ganCalMSRef + ganCalTechoRef + ganCalVentNRef + ganCalVentERef + ganCalVentORef + ganCalVentSRef
    ganCalTotMuroProy = ganCalMNProy + ganCalMEProy + ganCalMOProy + ganCalMSProy + ganCalTechoProy

    ganCalTotCondProy = ganCalTotMuroProy

    ganCalTotMuroRef = ganCalTotMuroRef + ganRadTotRef
    ganCalTotMuroProy = ganCalTotMuroProy + ganRadTotProy

    ganCalPorcentaje = ( ganCalTotMuroRef - ganCalTotMuroProy) / (ganCalTotMuroRef * -1)

    return  ganCalPorcentaje * 100