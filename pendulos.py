import numpy as np


# Funcion derivada para el pendulo simple

def simple(y, **kwargs):

    l = 1.

    g = 1.
    
    for key in kwargs:

        if key == 'l':

            l = kwargs[key]

        elif key == 'g':
            
            g = kwargs[key]

            
            
    yp = np.zeros(2)

    yp[0] = y[1]

    yp[1] = - g * np.sin(y[0]) / l

    # yp[1] = - g * y[0] / l

    return yp



def simplePeriod(theta, **kwargs):


    l = 1.

    g = 1.
    
    for key in kwargs:

        if key == 'l':

            l = kwargs[key]

        elif key == 'g':
            
            g = kwargs[key]


            
    
    acum = 0.

    for n in range(100):

        a = np.math.factorial(2*n) / ((2**n)*np.math.factorial(n))**2
        
        acum = acum + (a**2) * np.sin(0.5*theta)**(2*n)


    acum = acum  * 2. * np.pi * np.sqrt(l/g)

    return acum





def double(y, **kwargs):

    l1 = 1.

    l2 = 1.

    m1 = 1.

    m2 = 1.

    g = 10.
    
    for key in kwargs:

        if key == 'l1':

            l1 = kwargs[key]

        if key == 'l2':

            l2 = kwargs[key]

        if key == 'm1':

            m1 = kwargs[key]

        if key == 'm2':

            m2 = kwargs[key]   

        elif key == 'g':
            
            g = kwargs[key]

            
            
    yp = np.zeros(4)

    yp[0] = y[2]

    yp[1] = y[3]

    yp[2] = m2 * l2 * y[3]**2 * np.sin(y[1]-y[0]) - (m1+m2) * g * np.sin(y[0]) + m2 * np.cos(y[1]-y[0]) * ( l1 * y[2]**2 * np.sin(y[1]-y[0]) + g * np.sin(y[1]) )

    yp[2] = yp[2] / ( (m1+m2)*l1 - m2 * l1 * np.cos(y[1]-y[0])**2 )

    yp[3] = (  -l1 * y[2]**2 * np.sin(y[1]-y[0]) - g * np.sin(y[1]) - l1 * yp[2] * np.cos(y[1]-y[0])  )   /  l2

    return yp




def dobleEnergia(y, **kwargs):

    
    l1 = 1.

    l2 = 1.

    m1 = 1.

    m2 = 1.

    g = 10.
    
    for key in kwargs:

        if key == 'l1':

            l1 = kwargs[key]

        if key == 'l2':

            l2 = kwargs[key]

        if key == 'm1':

            m1 = kwargs[key]

        if key == 'm2':

            m2 = kwargs[key]   

        elif key == 'g':
            
            g = kwargs[key]


    T = np.zeros(len(y))

    V = np.zeros(len(y))
            

    for i,x in enumerate(y):
    
        T[i] = 0.5 * (m1+m2) * l1**2 * y[i][2]**2   +   0.5 * m2 * l2**2 * y[i][3]**2   +   m2 * l1 * l2 * y[i][2] * y[i][3] * np.cos(y[i][1]-y[i][0])

        V[i] = -(m1 + m2) * g * l1 * np.cos(y[i][0]) - m2 * g * l2 * np.cos(y[i][1])


    return T,V
