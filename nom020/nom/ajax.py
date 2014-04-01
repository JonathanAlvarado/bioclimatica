from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax

@dajaxice_register
def sayhello(request):
	return simplejson.dumps({'message':'Hello World'})

@dajaxice_register
def multiply(request, a, b):
	dajax = Dajax()
	result = int(a) * int(b)
	dajax.assign('#result','value',str(result))
	return dajax.json()

