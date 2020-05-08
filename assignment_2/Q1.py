# Mukesh Taank
# mtaank@uoguelph.ca
# USER: mtaank
# CTA 200H
# Question 1

import matplotlib.pyplot as plt
from math import sqrt as sq
import numpy as np

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
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    plt.xlabel('Real $(x)$')
    plt.ylabel('Imaginary $(y)$')
    plt.grid()
    plt.title("Complex Plane")
    plt.legend(loc='best')
    plt.show()
    return

n = 10 # Number of iterations
z0 = 0 # Initial position given z0 = 0


# Choose points, C, of the form c = x + iy
# Both x and y are bound by: -2 < x,y < 2
x_vals = [-0.2, 1.8, -0.6, 1.3, 0.4]
y_vals = [-0.4, 0.6, -0.234, 1.9, -0.3]
c_vals = [complex(x,y) for x,y in zip(x_vals, y_vals)]

#Initialize some matrices
Z = z0*np.zeros((len(c_vals),n), dtype=np.complex) #This will hold the values of z for each value of c
reals = np.zeros((len(c_vals),n)) #This holds all the real components of z
imags = np.zeros((len(c_vals),n)) #This holds all the imaginary components of z

for i in range(len(c_vals)):
    
    #Print out the modulus of each number C
    modulus_of_c = [sq(x**2+y**2) for x,y in zip(x_vals,y_vals)]
    print("modulus of " + str(c_vals[i]), "is: ", modulus_of_c[i])
    
    # Now calculate the values of Z for corresponding value of C
    for k in range(1,n):
        Z[i][k] = Z[i][k-1]**2 + c_vals[i]

        # Separate the values of Z into its real and imaginary parts for plotting
        reals[i][k] = Z[i][k].real
        imags[i][k] = Z[i][k].imag
        
# Arrange the graphs of each on the plot
# If the plot diverges - make red. If the plot is contained - make blue
plt.plot(reals[0], imags[0], 'b-', label="c = "+str(c_vals[0]))
plt.plot(reals[1], imags[1], 'r-', label="c = "+str(c_vals[1]))
plt.plot(reals[2], imags[2], 'b:', label="c = "+str(c_vals[2]))
plt.plot(reals[3], imags[3], 'r--', label="c = "+str(c_vals[3]))
plt.plot(reals[4], imags[4], 'b--', label="c = "+str(c_vals[4]))
plot_setup()
