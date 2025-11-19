import numpy as np
import math
np.set_printoptions(linewidth=200)


#initialization
h = 0.5 
r = 0.5
k = r*h

M = int((5 - (-1))/h) + 1
# since integrate up to two step 
N = 3

# initial condition function
def initial_condition(x):
    if(x < 0):
        return 0
    elif(x >= 0 and x < 2):
        return x/2
    elif(x >= 2 and x < 4):
        return 2 - (x/2)
    else: 
        return 0

# lax wendroff scheme
def lax_wendroff_scheme(u,i):
    return u[i] - r*(u[i+1] - u[i-1])/2 + r**2 * (u[i+1] + u[i-1] - 2*u[i]) / 2



# matrix formation
u = []
for n in range(N):
    u_n = []
    for i in range(n):
        u_n.append(0)
    for i in range(n,M-n):
        if(n == 0):
            u_n.append(initial_condition(i*h - 1))
        else:
            u_n.append(lax_wendroff_scheme(u[-1],i))
    for i in range(M-n,M):
        u_n.append(0)
    u.append(u_n)
u = np.matrix(u)

print(u)
    

