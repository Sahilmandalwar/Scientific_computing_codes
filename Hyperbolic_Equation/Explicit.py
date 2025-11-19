import numpy as np
import math

h = 1/4
r = 3/4
k = r*h

space_mesh = int(1/h) + 1
time_mesh = 6
u = np.zeros((time_mesh,space_mesh))

def boundry_initial_condition(i,n):
    if(i == 0 or i*h == 1):
        return 0
    elif(n == 0):
        return math.sin(math.pi*i*h)
    else:
        return 0

for n in range(6):
    for i in range(space_mesh):
        u[n,i] = boundry_initial_condition(i,n)
print(u)


# scheme applied
for n in range(time_mesh - 1):
    for i in range(1,space_mesh-1):
        if( n == 0):
            u[n+1,i] = (r**2*(u[n,i+1] + u[n,i-1]) + 2*(1-r**2)*u[n,i]) / 2
        else:
            u[n+1, i] = r**2*(u[n,i+1] + u[n,i-1]) + 2*(1-r**2)*u[n,i] - u[n-1,i]

print(u)

exact = np.zeros((time_mesh,space_mesh))
for n in range(time_mesh):
    for i in range(space_mesh):
        exact[n,i] = math.sin(math.pi*i*h)*math.cos(math.pi*n*k)
exact = np.matrix(exact)
print(exact)
print("---------"*10)
print(u - exact)
