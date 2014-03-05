import numpy as np

'''determina los valores atipicos de acuerdo al promedio de los datos (u)
la desviacion estandard de los datos (s) y una constante m que provee el numero
de desviaciones estandard a tomar en cuenta.
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