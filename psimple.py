import ODE

import numpy as np

import pendulos as pd

import matplotlib.pyplot as plt

if __name__ == "__main__":

    
    # Condicion inicial
    
    y0 = np.zeros(2)

    y0[0] = np.radians(0.1)




    # Condiciones de simulacion

    tf = pd.simplePeriod( y0[0] )

    orden = False



    if orden == False:
    

        # Condiciones de simulacion

        nt = 30

        tarray = np.linspace(0, tf, nt+1)

        fig, axs = plt.subplots(1, 2)



        # Euler Explicito

        y = ODE.theta( pd.simple, y0, tf/nt, nt, th = 0. )

        axs[0].plot( tarray, y[:,0], label = 'Euler Explícito' )

        axs[1].plot( tarray, y[:,1], label = 'Euler Explícito' )



        # Euler Implicito

        y = ODE.theta( pd.simple, y0, tf/nt, nt, th = 1. )

        axs[0].plot( tarray, y[:,0], label = 'Euler Implícito' )

        axs[1].plot( tarray, y[:,1], label = 'Euler Implícito' )


    
        # Crank-Nicholson
    
        y = ODE.theta( pd.simple, y0, tf/nt, nt, th = 0.5 )

        axs[0].plot( tarray, y[:,0], label = 'Crank-Nicholson' )

        axs[1].plot( tarray, y[:,1], label = 'Crank-Nicholson' )


        # Runge-Kutta 4

        y = ODE.RK4( pd.simple, y0, tf/nt, nt )

        axs[0].plot( tarray, y[:,0], label = 'Runge-Kutta 4' )

        axs[1].plot( tarray, y[:,1], label = 'Runge-Kutta 4' )
        


        # Grafico de theta
    
        axs[0].set_xlabel('t')

        axs[0].set_ylabel(r'$\theta$')

        axs[0].legend( loc = 'best' )

        axs[0].axhline(y0[0], linestyle = '--')
        
        axs[0].axhline(-y0[0], linestyle = '--')

    

        # Grafico de theta'
    
        axs[1].set_xlabel('t')

        axs[1].set_ylabel(r'$\frac{d\theta}{dt}$')

        axs[1].legend( loc = 'best' )


        plt.show()


    

    
    else:


        tlist = ( np.logspace(1,4,20) ).astype(int)



        # Array de error

        phaseError = np.zeros( (len(tlist), 4) )

        ampError =  np.zeros( (len(tlist), 4) )



    
        for i, nt in enumerate(tlist):

        
            # Euler explicito
        
            y = ODE.theta( pd.simple, y0, tf/int(nt), int(nt), th = 0. )

            ampError[i][0] = abs( np.linalg.norm(y[0]) - np.linalg.norm(y[-1]) )

            phaseError[i][0] = abs( np.arctan(y[-1][1]/y[-1][0]) )


            # Euler implicito
        
            y = ODE.theta( pd.simple, y0, tf/int(nt), int(nt), th = 1. )

            ampError[i][1] = abs( np.linalg.norm(y[0]) - np.linalg.norm(y[-1]) )

            phaseError[i][1] = abs( np.arctan(y[-1][1]/y[-1][0]) )

        

            # Crank-Nicholson
        
            y = ODE.theta( pd.simple, y0, tf/int(nt), int(nt), th = 0.5 )

            ampError[i][2] = abs( np.linalg.norm(y[0]) - np.linalg.norm(y[-1]) )

            phaseError[i][2] = abs( np.arctan(y[-1][1]/y[-1][0]) )


            # Runge-Kutta 4
        
            y = ODE.RK4( pd.simple, y0, tf/int(nt), int(nt) )

            ampError[i][3] = abs( np.linalg.norm(y[0]) - np.linalg.norm(y[-1]) )

            phaseError[i][3] = abs( np.arctan(y[-1][1]/y[-1][0]) )
        


        


        fig, axs = plt.subplots(1, 2)

        axs[0].loglog( tf / tlist, ampError[:,0], label = 'Euler Explícito')
    
        axs[0].loglog( tf / tlist, ampError[:,1], label = 'Euler Implícito')

        axs[0].loglog( tf / tlist, ampError[:,2], label = 'Crank-Nicholson')

        axs[0].loglog( tf / tlist, ampError[:,3], label = 'Runge-Kutta')

        axs[0].loglog( tf / tlist, tf / tlist, label = r'$O(h)$', linestyle = '--', color = 'k')

        # axs[0].loglog( tf / tlist, (tf / tlist)**2, label = r'$O(h^2)$', linestyle = ':', color = 'k')

        axs[0].loglog( tf / tlist, ampError[0][3] * 1.1 * (tf / tlist)**5, label = r'$O(h^5)$', linestyle = '-.', color = 'k')


        axs[0].set_xlabel('h')

        axs[0].set_ylabel(r'Error de amplitud')
            
        axs[0].legend( loc = 'best' )

        axs[0].grid()

    


    

        axs[1].loglog( tf / tlist, phaseError[:,0], label = 'Euler Explícito')
    
        axs[1].loglog( tf / tlist, phaseError[:,1], label = 'Euler Implícito')

        axs[1].loglog( tf / tlist, phaseError[:,2], label = 'Crank-Nicholson')

        axs[1].loglog( tf / tlist, phaseError[:,3], label = 'Runge-Kutta')

        axs[1].loglog( tf / tlist, tf / tlist, label = r'$O(h)$', linestyle = '--', color = 'k')

        axs[1].loglog( tf / tlist, (tf / tlist)**2, label = r'$O(h^2)$', linestyle = ':', color = 'k')

        axs[1].loglog( tf / tlist, (tf / tlist)**4, label = r'$O(h^4)$', linestyle = '-.', color = 'k')
    

        axs[1].set_xlabel('h')

        axs[1].set_ylabel(r'Error de fase')

        axs[1].legend( loc = 'best' )

        axs[1].grid()

    
        plt.show()        


        
