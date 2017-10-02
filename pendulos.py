import numpy as np


# Funcion derivada para el pendulo simple

def simple(y,g,l):

    yp = np.zeros(2)

    yp[0] = y[1]

    yp[1] = - g * np.sin(y[0]) / l

    # yp[1] = - g * y[0] / l

    return yp


def simplePeriod(theta, l = 1., g = 1.):

    acum = 0.

    for n in range(100):

        a = np.math.factorial(2*n) / ((2**n)*np.math.factorial(n))**2
        
        acum = acum + (a**2) * np.sin(0.5*theta)**(2*n)


    acum = acum  * 2. * np.pi * np.sqrt(l/g)

    return acum
