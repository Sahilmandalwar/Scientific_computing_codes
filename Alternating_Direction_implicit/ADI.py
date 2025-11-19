import numpy as np
import math

# initialization
h = 1/3
alpha = 1
k = alpha * h**2
space_mesh = int(1/h) + 1

# tri-diagonal 
tri_left_half = np.matrix(np.diag([1+alpha]*(space_mesh-2),0) + np.diag([-alpha/2]*(space_mesh-3),1) + np.diag([-alpha/2]*(space_mesh-3),-1))
tri_left_full = np.matrix(np.diag([1+alpha]*(space_mesh-2),0) + np.diag([-alpha/2]*(space_mesh-3),1) + np.diag([-alpha/2]*(space_mesh-3),-1))
# boundry initial condition 
def initial_boundry_condition(x,y,n):
    if(x == 0 or y == 0 or x * h == 1 or y*h == 1):
        return 0
    elif(n == 0):
        return math.sin(2*math.pi*x*h) * math.sin(2*math.pi*y*h)
    else:
        return 0

# ADI n+1/2 function
def half_time_step_adi(u,j):
    u_right = []
    for i in range(1,space_mesh-1): # right side matrix
        u_right.append((1-alpha)*u[j,i] + alpha*(u[j+1,i] + u[j-1,i])/2)
    u_right = np.matrix(u_right)
    u_right[0,0] -= u[j,0]
    u_right[0,-1] -= u[j,-1]
    return np.linalg.solve(tri_left_half,u_right.T)

# ADI n+1 function
def full_time_step_adi(u,i):
    u_right = []
    for j in range(1,space_mesh-1):
        u_right.append((1-alpha)*u[j,i] + alpha*(u[j,i+1] + u[j,i-1])/2)
    u_right = np.matrix(u_right)
    u_right[0,0] -= u[0,i]
    u_right[0,-1] -= u[-1,i]
    return np.linalg.solve(tri_left_full,u_right.T)

        
# matrix initialization
u = []
for y in range(space_mesh):
    u_y = []
    for x in range(space_mesh):
        u_y.append(initial_boundry_condition(x,y,0))
    u.append(u_y)
u = np.matrix(u)
print(u)
print()
# matrix filling for n+half time step
u_new = u.copy()
for j in range(1,space_mesh-1):
    u_new[j,1:-1] = half_time_step_adi(u,j).T
u = u_new
print(u)
print()
# matrix filling for n+1 time step
u_new = u.copy()
for i in range(1,space_mesh-1):
    u_new[1:-1,i] = full_time_step_adi(u,i)
u = u_new
print(u)

