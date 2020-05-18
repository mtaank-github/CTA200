# Mukesh Taank
# mtaank@uoguelph.ca
# USER: mtaank
# CTA 200H
# Question 2

import numpy as np
import scipy
from scipy.integrate import odeint #Scipy's built-in function for solving ODEs
import matplotlib.pyplot as plt

def SIR(y, t, gamma, beta, N):
    '''
    Description:
    Sets up the plotting parameters for the graph we want to create. Need to call plt.plot()
    before calling this function.
    
    Parameters:
    y - dummy variable to contain the S, I, R functions - a list
    t - time - a list
    gamma -  parameter representing the recovery rate
    beta - paramter representing the infection rate - a float
    N - Number of people in the population - an integer
    
    Returns:
    This will return the differential equations needed to be solved later on and arranges \
    them into a list.
    '''
    S, I, R = y #Put all our functions into one list called y
    
    # Now put the ODEs into a list of the form: dy/dt = [dS/dt, dI/dt, DR/dt]
    dy_dt = [-(beta*S*I)/N, (beta*S*I)/N - gamma*I, gamma*I]
    
    return dy_dt

def plot_setup():
    '''
    Description:
    Sets up the plotting parameters for the graph we want to create. Need to call plt.plot() \
    before calling this function Sets the title, axes, x and y limits, legend and gridlines.
    
    Parameters:
    No parameters
    
    Returns:
    No return
    '''
    plt.xlim(0,200)
    plt.ylim(0,1000)
    plt.xlabel('time, $t$')
    plt.ylabel('Number of People')
    plt.grid()
    plt.title(r'Plot of the solution to the SIR model with $\beta$ = 1/4 and $\gamma$ = 1/3')
    plt.legend(loc='best')
    plt.show()
    return


# Now we can make choose our constants
N = 1000
beta = 1/4
gamma = 1/3

# Now need intital conditions for the S, I, R
# Set up list as [S(0), I(0), R(0)]
# We are given that:
# S(0)=999, I(0)=1, R(0)=0
y0 = [999., 1., 0.]

# We need to integrate from t=0 to t=200
t = np.linspace(0,200,101)

# Now can use the scipy function odeint to get the solutions for S, I and R
solutions = odeint(SIR, y0, t, args=(beta, gamma,N))

# Now we can plot the solution curves
plt.plot(t, solutions[:,0], 'r-', label='S(t) Number of People Susceptible')
plt.plot(t, solutions[:,1], 'b-', label='I(t) Number of People Infected')
plt.plot(t, solutions[:,2], 'g-', label='R(t) Number of People Recovered')
plot_setup()





