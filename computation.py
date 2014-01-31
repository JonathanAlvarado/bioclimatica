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

def get_all(table, solution = False):
    if solution:
        query = "SELECT * FROM %s WHERE descripcion='%s'" % (table,solution)
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

    city_data = get_all("ciudades")
    print city_data

    for i in solutions:
        solutions_details = get_all("soluciones")
        

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