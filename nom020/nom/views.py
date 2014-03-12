from django.shortcuts import render
from nom.models import soluciones

# Create your views here.
def index(request):
	sol = soluciones.objects.all()
	context = {'title':'prueba', 'content':'prueba', 'solucion': sol }
	return render(request, 'nom/index.html', context)