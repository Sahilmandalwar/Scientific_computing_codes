# given problem         y`` = 3/2*y**2       y(0) = 4 and y(1) = 1


import numpy as np
import math

# initialization
h = 0.1
step_size = int(1/h) + 1
initial_value = 4 - 3*np.linspace(0,1,step_size) # value at k = 0
error_tollerence = 0.0001

# since the tri-diagonal contain a term which is changing so it is break in two part 
fixed_tri = np.diag([-2]*(step_size-2),0) + np.diag([1]*(step_size-3),1) + np.diag([1]*(step_size-3),-1) 
print(fixed_tri)


while True:

    y_old_in = initial_value[1:-1].copy()   # value at K is used to make y_old_in
    rhs = -3/2*h**2*y_old_in**2             # rhs of the equation
    rhs[0] -= 4 
    rhs[-1] -= 1                            # know term from left hand side 

    adjusted_diag = np.diag(y_old_in,0)     # second part of tri diagonal 
    tri_diag = fixed_tri - 3*h**2*adjusted_diag # complete tri diagonal 

    new_value = np.linalg.solve(tri_diag,rhs)   # values at k+1 is found 
  
    error = max(abs(new_value - initial_value[1:-1]))   # the error is found to break out of loop
    if(error <= error_tollerence):
        break

    initial_value[1:-1] = new_value         # now values at k+1 will be used to find the next iteration value

print(new_value)