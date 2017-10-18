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

    # mode = 'simple'
    
    mode = 'animacion'

    # mode = 'caos'              

    # mode = 'energia'

    

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




    elif mode == 'animacion':


        tf = 10 * np.pi
        
        h = 0.01

        nt = int(tf/h)

        h = tf/nt

        aList = [ np.pi * 0.5, 1.00001 * np.pi * 0.5, 0.99999 * np.pi * 0.5 ]


        x1 = np.zeros((nt+1,len(aList)))

        x2 = np.zeros((nt+1,len(aList)))

        y1 = np.zeros((nt+1,len(aList)))

        y2 = np.zeros((nt+1,len(aList)))

        
        for i,a in enumerate(aList):

            y0[1] = a

            y = ODE.RK4( pd.double, y0, h, nt ) 

            x1[:,i] =  np.sin(y[:,0]) 

            y1[:,i] = -np.cos(y[:,0]) 

            x2[:,i] =  np.sin(y[:,1]) + x1[:,i]
            
            y2[:,i] = -np.cos(y[:,1]) + y1[:,i]




            
        

        fig, ax = plt.subplots()

        time_template = 'time = %.1f $\pi$'
        
        ax.set_xlim(-2.5, 2.5)

        ax.set_ylim(-2.5, 1)
        
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

       


        l1, = plt.plot([], [], 'o-', markersize = 10, animated=True)

        l2, = plt.plot([], [], 'o-', markersize = 10, animated=True)

        l3, = plt.plot([], [], 'o-', markersize = 10, animated=True)



        plt.xticks([])

        plt.yticks([])
            

            



        def update(frame, line1, line2, line3, ttext):



            thisx = [0, x1[int(frame)][0], x2[int(frame)][0]]

            thisy = [0, y1[int(frame)][0], y2[int(frame)][0]]            
    
            line1.set_data(thisx, thisy)

            
            thisx = [0, x1[int(frame)][1], x2[int(frame)][1]]

            thisy = [0, y1[int(frame)][1], y2[int(frame)][1]]            
    
            line2.set_data(thisx, thisy)
            


            thisx = [0, x1[int(frame)][2], x2[int(frame)][2]]

            thisy = [0, y1[int(frame)][2], y2[int(frame)][2]]            
    
            line3.set_data(thisx, thisy)
    

            ttext.set_text(time_template%(frame*h/np.pi))
            
            
            return line1, line2, line3, ttext



        
        ani = animation.FuncAnimation(fig, update, np.arange(1,nt),fargs = (l1, l2, l3, time_text), interval=10,  blit=True)


        
        plt.show()








    elif mode == 'energia':

        
        tf = 2. * np.pi

        ntList = ( np.logspace(3,5,20) ).astype(int)

        energyError = []
        
            
        for nt in ntList:
            
        
            y = ODE.RK4( pd.double, y0, tf/int(nt), int(nt) )

            T, V = pd.dobleEnergia(y)

            energyError.append( abs(T[-1] + V[-1]) )
        


        hList = tf/ntList

        plt.loglog(hList, energyError, label = 'RK-4')

        plt.loglog(hList, energyError[0] * hList**4 / hList[0]**4, label = r'$O(h^4)$', linestyle = '--', color = 'k')

        plt.loglog(hList, energyError[0] * hList**5  / hList[0]**5, label = r'$O(h^5)$', linestyle = '-.', color = 'k')

        plt.legend( loc='best' )

        plt.xlabel('$h$')

        plt.ylabel('$E(10\pi)-E(0)$')

        plt.show()
