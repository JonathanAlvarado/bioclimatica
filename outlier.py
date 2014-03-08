import numpy as np

'''determina los valores atipicos de acuerdo al promedio de los datos (u)
la desviacion estandard de los datos (s) y una constante m que provee el numero
de desviaciones estandard a tomar en cuenta.
https://groups.google.com/forum/#!topic/comp.lang.python/z1da1ldxNlo
http://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list

'''
def outliers(data):
    m = 2
    u = np.mean(data)#promedio de los datos
    s = np.std(data)#desviacion estandard
    result = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return result

d = [2,4,5,1,6,5,40]
out = outliers(d)
print out