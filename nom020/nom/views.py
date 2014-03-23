from django.shortcuts import render
from nom.models import soluciones, ciudades, estados
from forms import cityForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	sol = soluciones.objects.all()
	edos = estados.objects.values('estado').distinct()
	form = cityForm()
	#context = {'title':'prueba', 'content':'prueba', 'solucion': sol, 'estados': edos }
	context = {'title':'prueba', 'form':form}
	return render(request, 'nom/index.html', context)