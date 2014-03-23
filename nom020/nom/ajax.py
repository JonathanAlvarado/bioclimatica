from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})