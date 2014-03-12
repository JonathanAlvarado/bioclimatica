from django.shortcuts import render
from nom.models import soluciones, ciudades

# Create your views here.
def index(request):
	sol = soluciones.objects.all()
	edos = ciudades.objects.values('estado').distinct()
	context = {'title':'prueba', 'content':'prueba', 'solucion': sol, 'estados': edos }
	return render(request, 'nom/index.html', context)