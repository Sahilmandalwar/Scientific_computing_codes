import numpy as np
import math

# initialization
h = 1/3
k = 1/18
c = 1
alpha = c**2*k/h**2
space_mesh = math.ceil(1/h) + 1
time_mesh = 5

# Scheme defination
def scheme_ftcs(u,n,i):
    return (1-2*alpha)*u[n,i] + alpha*(u[n,i-1] + u[n,i+1])

# boundry condition 
def boundry_initial_condition(n,i):
    if(((i * h) == 0) or ((i * h) == 1)):
        return 0
    elif(n == 0):
        return math.sin(i*h*math.pi)
    else:
        return 0

# matrix formation
u = []
for n in range(time_mesh):
    u_n = []
    for i in range(space_mesh):
        u_n.append(boundry_initial_condition(n,i))
    u.append(u_n)
u = np.matrix(u)

# scheme applied
for n in range(1,time_mesh):
    for i in range(1,space_mesh - 1):
        u[n,i] = scheme_ftcs(u,n-1,i)

print(u)


