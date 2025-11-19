import numpy as np
import math

# initialization
h = 1/3
k = 1/9
c = 1
alpha = c**2*k/h**2
space_mesh = int(1/h) + 1
time_mesh = 5

# initial_boundry_condition
def initial_boundry_condition(n,i):
    if(i == 0 or i*h == 1):
        return 0
    elif(n == 0):
        return math.sin(math.pi*i*h)
    else:
        return 0

# tri-diagonal matrix
left_tri  = np.diag([1+alpha]*(space_mesh-2),k=0) + np.diag([-alpha/2]*(space_mesh-3),k=1) + np.diag([-alpha/2]*(space_mesh-3), k=-1)
right_tri = np.diag([1-alpha]*(space_mesh-2), k=0) + np.diag([alpha/2]*(space_mesh-3), k=1) + np.diag([alpha/2]*(space_mesh-3), k=-1)

# matrix_initialization
u = []
for n in range(time_mesh):
    u_n = []
    for i in range(space_mesh):
        u_n.append(initial_boundry_condition(n,i))
    u.append(u_n)
u = np.matrix(u)

def crank_nicholson(u,n):
    u_right = u[n-1,1:-1].copy()
    right_matrix = np.dot(right_tri,u_right.T) 
    right_matrix[0,0] += ((alpha*(u[n,0])/2) - alpha*(u[n-1,0])/2)
    right_matrix[0,-1] += ((alpha*(u[n,-1])/2) - alpha*(u[n-1,-1])/2)
    
    return np.linalg.solve(left_tri,right_matrix)

# scheme applied
for n in range(1,time_mesh):
    u[n,1:-1] = crank_nicholson(u,n).T
print(u)


