from django.shortcuts import render
from nom.models import soluciones, ciudades, estados
from forms import data_form
from django.core import serializers


# Create your views here.
def index(request):
	#context = {'title':'prueba', 'content':'prueba', 'solucion': sol, 'estados': edos }
	context = {'title':'prueba'}
	return render( request, 'nom/index.html', context )

def index2(request):
	form = data_form()
	context = {'title':'prueba', 'form':form, 'result': '--'}
	return render( request, 'nom/index2.html', context )