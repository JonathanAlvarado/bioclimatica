#!/usr/bin/python
#-*- coding: utf-8 -*-
import MySQLdb as mdb
import sys

def get_k(state, city, floors):
    if(floors <= 3):
        query = "SELECT kref_3niv FROM ciudades WHERE estado='%s' AND ciudad='%s'" %(state, city)
        cursor.execute(query)
        data = cursor.fetchall()
        k_roof = data[0][0]
        k_wall = data[0][0]

    elif(floors > 3):
        query = "SELECT kref_mas3niv_techo,kref_mas3niv_pared FROM ciudades WHERE estado='%s' AND ciudad='%s'" %(state, city)
        cursor.execute(query)
        data = cursor.fetchall()
        k_roof = data[0][0]
        k_wall = data[0][1]
    return k_roof,k_wall

def get_R(solution):
    query = "SELECT valorR FROM soluciones WHERE descripcion='%s'" % (solution)
    cursor.execute(query)
    data = cursor.fetchall()
    value_R = data[0][0]
    return value_R

def get_all(table, solution = False, city = False):
    if solution:
        query = "SELECT * FROM %s WHERE descripcion='%s'" % (table,solution)
    elif city:
        query = "SELECT * FROM %s WHERE ciudad='%s'" % (table,city)
    else:
        query = "SELECT * FROM %s" % (table)
    cursor.execute(query)
    data = cursor.fetchall()
    return data

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

    city_data = get_all("ciudades", city = city)
    
    for i in range( len(solutions) ):
        solutions_details = get_all("soluciones")

        if solutions[i][0] == "techo":
            if solutions[i][1] == "Superficie Inferior":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][7] - city_data[0][6] ) )
            elif solutions[i][1] == "Techo":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][8] - city_data[0][6] ) )
            elif solutions[i][1] == "Domo":
                ganCalTechoProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][17] - city_data[0][6] ) )
                
                ganRadVentTechoProy += ( solutions_details[0][6] * solution[i][3] * city_data[0][22] - solutions_details[0][5]);

        elif solutions[i][0] == "muroNorte":
            if solutions[i][1] == "Ventana":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][18] - city_data[0][6] ) )
                
                ganRadVentNProy += ( solutions_details[0][6] * solutions[i][2] * city_data[0][23] * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][9] - city_data[0][6] ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMNProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][13] - city_data[0][6] ) )
        
        elif solutions[i][0] == "muroEste":
            if solutions[i][1] == "Ventana":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][19] - city_data[0][6] ) )
                
                ganRadVentEProy += ( solutions_details[0][6] * solutions[i][2] * city_data[0][24] * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][10] - city_data[0][6] ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][14] - city_data[0][6] ) )

        elif solutions[i][0] == "muroSur":
            if solutions[i][1] == "Ventana":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][21] - city_data[0][6] ) )
                
                ganRadVentSProy += ( solutions_details[0][6] * solutions[i][2] * city_data[0][26] * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][12] - city_data[0][6] ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMSProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][16] - city_data[0][6] ) )
        

        elif solutions[i][0] == "muroOeste":
            if solutions[i][1] == "Ventana":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][20] - city_data[0][6] ) )
                
                ganRadVentEProy += ( solutions_details[0][6] * solutions[i][2] * city_data[0][25] * solutions_details[0][5] )
            
            elif solutions[i][0] == "Muro Masivo":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][11] - city_data[0][6] ) )
                
            elif solutions[i][0] == "Muro Ligero":
                ganCalMEProy += ( (1 / get_R( solutions[i][3] ) ) * solutions[i][2] * ( city_data[0][15] - city_data[0][6] ) )

    print city_data[0][29]
    ganRadVentTechoRef += ( cgsRef * areaTecho * (0) * city_data[0][22] )
    ganCalTechoRef += ( k[0] * areaTecho * ( 1 - (0) ) * ( city_data[0][8] - city_data[0][6] ) )
    coConducTecho = ganCalTechoProy - ganCalTechoRef

    ganRadVentNRef += ( cgsRef * areaMN * ( fcRef ) * city_data[0][23] )
    ganCalMNRef += ( k[1] * areaMN * (1 - ( fcRef )) * ( city_data[0][9 ] - city_data[0][6] ) )
    ganCalVentNRef = k[0] * areaMN * (fcRef) * ( city_data[0][18] - city_data[0][6] )
    coConducMN = ganCalMNProy - ganCalMNRef

    ganRadVentERef += ( cgsRef * areaME * ( fcRef ) * city_data[0][24] );
    ganCalMERef += ( k[1] * areaME * (1 - ( fcRef ) ) * ( city_data[0][10] - city_data[0][6] ) )
    ganCalVentERef = k[0] * areaME * ( fcRef ) * (city_data[0][19] - city_data[0][6] )

    ganRadVentSRef += ( cgsRef * areaMS * ( fcRef ) * city_data[0][26]);
    ganCalMSRef += ( k[1] * areaMS * (1 - ( fcRef ) ) * ( city_data[0][12 ] - city_data[0][6] ) );
    ganCalVentSRef = k[0] * areaMS * ( fcRef ) * ( city_data[0][21] - city_data[0][6] )

    ganRadVentORef += ( cgsRef * areaMO * ( fcRef ) * city_data[0][25]);
    ganCalMORef += ( k[1] * areaMO * (1 - ( fcRef ) ) * ( city_data[0][11] - city_data[0][6] ) );
    ganCalVentORef = k[0] * areaMO * ( fcRef ) * ( city_data[0][20] - city_data[0][6] )

    ganRadTotRef = ganRadVentNRef + ganRadVentERef + ganRadVentORef + ganRadVentSRef + ganRadVentTechoRef
    ganRadTotProy = ganRadVentNProy + ganRadVentEProy + ganRadVentOProy + ganRadVentSProy + ganRadVentTechoProy

    ganCalTotMuroRef = ganCalMNRef + ganCalMERef + ganCalMORef + ganCalMSRef + ganCalTechoRef + ganCalVentNRef + ganCalVentERef + ganCalVentORef + ganCalVentSRef
    ganCalTotMuroProy = ganCalMNProy + ganCalMEProy + ganCalMOProy + ganCalMSProy + ganCalTechoProy

    ganCalTotCondProy = ganCalTotMuroProy

    ganCalTotMuroRef = ganCalTotMuroRef + ganRadTotRef
    ganCalTotMuroProy = ganCalTotMuroProy + ganRadTotProy

    ganCalPorcentaje = ( ganCalTotMuroRef - ganCalTotMuroProy) / (ganCalTotMuroRef * -1)

    print  ganCalPorcentaje * 100



try:
    con = mdb.connect(host='localhost', user='root', passwd='root', db='calcio73_nom020')
    cursor = con.cursor()
    state = 'Zacatecas'
    city = 'Fresnillo'
    floors = 4
    #tipo,solucion,area,porcion
    solutions = [['muroNorte','Ejemplo Muro',20,'Muro Masivo'],['muroNorte','Ejemplo Muro',20,'Muro Masivo']]
    #k = get_k(state, city, floors)
    #value_R = get_R(solution)
    #print get_all("soluciones")
    calculate(state, city, floors,solutions)
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()
