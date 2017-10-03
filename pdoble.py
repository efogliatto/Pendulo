import ODE

import numpy as np

import pendulos as pd

import matplotlib.pyplot as plt


if __name__ == "__main__":

    
    # Condicion inicial
    
    y0 = np.zeros(4)

    y0[0] = np.pi * 0.5

    y0[1] = np.pi * 0.5




    # Condiciones de simulacion

    mode = 'caos'

    

    if mode == 'simple':

        
        tf = np.pi
    
        nt = 1200

        h = tf / nt

        tarray = np.linspace(0, tf, nt+1)

    

        # Runge-Kutta 4

        y = ODE.RK4( pd.double, y0, h, nt )



        plt.plot( tarray, y[:,0], label = r'$\theta_1$' )

        plt.plot( tarray, y[:,1], label = r'$\theta_2$' )

        plt.plot( tarray, y[:,2], label = r'$\dot{\theta}_1$' )

        plt.plot( tarray, y[:,3], label = r'$\dot{\theta}_2$' )
        

    
        # Grafico de theta
        
        plt.xlabel('t')

        plt.ylabel('variables')

        plt.legend( loc = 'best' )


        plt.show()



    elif mode == 'convergencia':


        # ntList = [300, 600, 1200, 2400]

        tf = np.pi

        ntList = [20, 40, 60, 80, 100]

        fig, axs = plt.subplots(2, 2)

        plt.xlabel('$t$')

        axs[0][0].set_ylabel( r'$\theta_1$' )

        axs[0][1].set_ylabel( r'$\theta_2$' )

        axs[1][0].set_ylabel( r'$\dot{\theta}_1$' )

        axs[1][1].set_ylabel( r'$\dot{\theta}_2$' )

        

        for nt in ntList:

            
            h = tf / nt

            tarray = np.linspace(0, tf, nt+1)

            y = ODE.RK4( pd.double, y0, h, nt )



            axs[0][0].plot( tarray, y[:,0], label = '{}'.format(nt) )

            axs[0][1].plot( tarray, y[:,1], label = '{}'.format(nt) )

            axs[1][0].plot( tarray, y[:,2], label = '{}'.format(nt) )

            axs[1][1].plot( tarray, y[:,3], label = '{}'.format(nt) )

            


        axs[0][0].legend( loc = 'best' )

        axs[0][1].legend( loc = 'best' )

        axs[1][0].legend( loc = 'best' )

        axs[1][1].legend( loc = 'best' )

        plt.show()



        
    elif mode == 'caos':

        
        aList = [ np.pi * 0.5, 1.00001 * np.pi * 0.5, 0.99999 * np.pi * 0.5 ]

        tf = 10 * np.pi
        
        h = 0.001

        nt = int(tf/h)

        h = tf/nt

        tarray = np.linspace(0, tf, nt+1)
        
        

        fig, axs = plt.subplots(2, 2)

        

        plt.xlabel('$t$')

        axs[0][0].set_ylabel( r'$\theta_1$' )

        axs[0][1].set_ylabel( r'$\theta_2$' )

        axs[1][0].set_ylabel( r'$\dot{\theta}_1$' )

        axs[1][1].set_ylabel( r'$\dot{\theta}_2$' )

        

        for a in aList:

            y0[1] = a

            y = ODE.RK4( pd.double, y0, h, nt )



            axs[0][0].plot( tarray, y[:,0], label = '{}'.format(a) )

            axs[0][1].plot( tarray, y[:,1], label = '{}'.format(a) )

            axs[1][0].plot( tarray, y[:,2], label = '{}'.format(a) )

            axs[1][1].plot( tarray, y[:,3], label = '{}'.format(a) )

            


        axs[0][0].legend( loc = 'best' )

        axs[0][1].legend( loc = 'best' )

        axs[1][0].legend( loc = 'best' )

        axs[1][1].legend( loc = 'best' )

        plt.show()
