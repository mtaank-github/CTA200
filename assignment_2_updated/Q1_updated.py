# Mukesh Taank
# mtaank@uoguelph.ca
# USER: mtaank
# CTA 200H
# Question 1

import matplotlib.pyplot as plt
import numpy as np
import cmath

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
    plt.legend(loc='upper right')
    plt.show()
    return

###################################################################################################

# Choose points, C, of the form c = x + iy
# Both x and y are bound by: -2 < x,y < 2

x_vals = np.linspace(-2.,2.,1000)
y_vals = np.linspace(-2.,2.,1000)
limit = np.sqrt(2**2 + 2**2)
N = 10 # Number of iterations

###################################################################################################
'''
# Part 1, plot the points C, but if the iterations diverge, make black. If they converge, then make white
c_conv_real_part1 = []
c_div_real_part1 = []
c_conv_imag_part1 = []
c_div_imag_part1  = []

for x in x_vals:
    for y in y_vals:
        
        c = complex(x,y)
        z = 0.*1j
        
        for i in range(N):
            z = z**2 + c
             
        if abs(z) < limit:
            c_conv_real_part1.append(c.real)
            c_conv_imag_part1.append(c.imag)
        else:
            c_div_real_part1.append(c.real)
            c_div_imag_part1.append(c.imag)

plt.scatter(c_conv_real_part1, c_conv_imag_part1, c="white", label="Convergent Points")
plt.scatter(c_div_real_part1, c_div_imag_part1, c="black", label="Divergent Points")
plot_setup()
plt.show()

###################################################################################################
'''
# Part 2: Add a colour bar so that the colour of the points shows the iteration number
c_converge_reals_part2 = []
c_converge_imags_part2 = []
c_diverge_reals_part2 = []
c_diverge_imags_part2 = []
iter_num_list = [] # To record iteration number of the divergence

for x in x_vals:
    for y in y_vals:
        
        c = complex(x,y)
        z = 0.*1j
        iter_num = 1
        
        for i in range(N):
            z = z**2 + c
            
            if abs(z) < limit:
                iter_num += 1
                
        if abs(z) > limit:
            iter_num_list.append(iter_num)
            c_diverge_reals_part2.append(c.real)
            c_diverge_imags_part2.append(c.imag)
            
        else:
            c_converge_reals_part2.append(c.real)
            c_converge_imags_part2.append(c.imag)
            
plt.scatter(c_converge_reals_part2,c_converge_imags_part2, c = "red", label = "convergent points")
plt.scatter(c_diverge_reals_part2,c_diverge_imags_part2, c= iter_num_list)
plt.colorbar(label="Iteration Number")
plot_setup()
plt.show()
