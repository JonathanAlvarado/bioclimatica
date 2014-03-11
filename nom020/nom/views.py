from django.shortcuts import render


# Create your views here.
def index(request):
	context = {'title':'prueba', 'content':'prueba'}
	return render(request, 'nom/index.html', context)