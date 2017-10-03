import ODE

import numpy as np

import pendulos as pd

import matplotlib.pyplot as plt

import matplotlib.animation as animation


if __name__ == "__main__":

    
    # Condicion inicial
    
    y0 = np.zeros(4)

    y0[0] = np.pi * 0.5

    y0[1] = np.pi * 0.5




    # Condiciones de simulacion

    # mode = 'animation'

    # mode = 'caos'              

    mode = 'energia'

    

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
        
        h = 0.01

        nt = int(tf/h)

        h = tf/nt

        tarray = np.linspace(0, tf, nt+1)
        
        

        fig, axs = plt.subplots(2, 2)

        



        axs[0][0].set_xlabel( '$t$' )

        axs[0][1].set_xlabel( '$t$' )

        axs[1][0].set_xlabel( '$t$' )

        axs[1][1].set_xlabel( '$t$' )
        
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




    elif mode == 'animation':


        tf = 10 * np.pi
        
        h = 0.001

        nt = int(tf/h)

        h = tf/nt



        aList = [ np.pi * 0.5, 1.00001 * np.pi * 0.5, 0.99999 * np.pi * 0.5 ]

        fig = plt.figure()
        
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1))
        

        for a in aList:

            y0[1] = a

            y = ODE.RK4( pd.double, y0, h, nt )
        
        

            x1 = np.sin(y[:,0])

            y1 = -np.cos(y[:,0])

            x2 = np.sin(y[:,1]) + x1

            y2 = -np.cos(y[:,1]) + y1

        
            # fig = plt.figure()
        
            # ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1))

            # ax.grid()
        
            line, = ax.plot([], [], 'o-', lw=1, markersize = 10)
        
            time_template = 'time = %.1fs'

            time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

            def init():
                line.set_data([], [])
                time_text.set_text('')
                return line, time_text

            def animate(i):
                thisx = [0, x1[i], x2[i]]
                thisy = [0, y1[i], y2[i]]

                line.set_data(thisx, thisy)
                time_text.set_text(time_template%(i*h))
                return line, time_text

        
            ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                                          interval=25, blit=True, init_func=init)


            #ani.save('double_pendulum.mp4', fps=15)

            
        plt.show()








    elif mode == 'energia':

        
        tf = 10 * np.pi
        
        hList = np.logspace(-4, -1, 20)

        ntList = np.zeros( len(hList) )

        for i,h in enumerate(hList):

            ntList[i] = int(tf/h)
            
            hList[i] = tf/ntList[i]

        

        energyError = []
            
        for nt,h in zip(ntList, hList):
            
        
            y = ODE.RK4( pd.double, y0, h, int(nt) )

            T,V = pd.dobleEnergia(y)

            energyError.append( abs(T[-1] + V[-1]) )
        

            

        plt.loglog(hList, energyError, label = 'RK-4')

        plt.loglog(hList, 2*hList**4, label = r'O(h^4)', linestyle = '--', color = 'k')

        plt.loglog(hList, 2*hList**5, label = r'O(h^5)', linestyle = '-:', color = 'k')

        plt.legend(loc='best')

        plt.show()
