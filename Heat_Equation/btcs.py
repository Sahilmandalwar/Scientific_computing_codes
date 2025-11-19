import numpy as np
import math 

# initialization
h = 1/3
k = 1/18
c = 1
alpha = c**2*k/h**2
space_mesh = math.ceil(1/h) + 1
time_mesh = 5

# tri-diagonal matrix
tri = np.matrix(np.diag([1+2*alpha]*(space_mesh-2),k=0) + np.diag([-alpha]*(space_mesh-3),k=1) + np.diag([-alpha]*(space_mesh-3),k=-1))
print(tri)

# initial and boundry condition applied
def initial_boundry_condition(i,n):
    if(i == 0 or i * h == 1):
        return 0
    elif(n == 0):
        return math.sin(i*h*math.pi)
    else:
        return 0

# btcs operation
def btcs_function(u,n):
    # RHS matrix
    u_temp = u[n-1,1:-1].copy()
    u_temp[0,0]  -= u[n,0]
    u_temp[0,-1] -=  u[n,-1]
    return np.linalg.solve(tri,u_temp.T)
   

# matrix initialization
u = []
for n in range(time_mesh):
    u_n = []
    for i in range(space_mesh):
        u_n.append(initial_boundry_condition(i,n))
    u.append(u_n)
u = np.matrix(u)

# scheme applied
for n in range(1,time_mesh):
    u[n,1:-1] = btcs_function(u,n).T

print(u)









