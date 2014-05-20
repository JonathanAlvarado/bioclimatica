# -*- coding: utf-8 -*-
from django.shortcuts import render
import data_analysis as dt

# Create your views here.
def index(request):
	data = dt.read_data()
	freq = dt.discretized_data( data )
	context = {'title': 'Análisis de datos','data': freq}
	return render( request, 'analytics/index.html', context )	