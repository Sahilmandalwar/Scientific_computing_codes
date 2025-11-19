import numpy as np
import math

h = 1/4
r = 3/4
k = r*h

space_mesh = int(1/h) + 1
time_mesh = 6
u = np.zeros((time_mesh, space_mesh))

# boundry condition
def boundry_initial_condition(i, n):
    if (i == 0 or i*h == 1):
        return 0
    elif (n == 0):
        return math.sin(math.pi*i*h)
    else:
        return 0

# tri-diagonal
tri = np.matrix(np.diag([1+r**2]*(space_mesh-2),k=0) + np.diag([-r**2/2]*(space_mesh-3),k=1) + np.diag([-r**2/2]*(space_mesh-3),k=-1))
print(tri)
# implicit scheme 
def implicit_scheme(u,n):
    u_temp = []
    if(n == 0):
        for i in range(1,space_mesh-1):
            u_temp.append(u[n,i])
        u_temp[0] += r**2/2*(u[n+1,0])
        u_temp[-1] += r**2 / 2 *(u[n+1,-1])
        u_temp = np.matrix(u_temp)
        return np.linalg.solve(tri,u_temp.T)
    else:
        for i in range(1,space_mesh-1):
            u_temp.append(2*u[n,i] + r**2*(u[n-1,i+1] + u[n-1,i-1])/2 - (r**2 + 1)*u[n-1,i])
        u_temp[0] += r**2/2*(u[n + 1,0])
        u_temp[-1] += r**2/2*(u[n+1,-1])
        u_temp = np.matrix(u_temp)
        return np.linalg.solve(tri,u_temp.T)


    return np.linalg.solve(tri,u_temp.T)

for n in range(time_mesh):
    for i in range(space_mesh):
        u[n,i] = boundry_initial_condition(i,n)
for n in range(time_mesh-1):
    u[n+1,1:-1] = implicit_scheme(u,n).T

print(u)



