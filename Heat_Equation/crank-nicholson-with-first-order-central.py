import numpy as np
import math

h = 1/3
r = 1/3
k = r*h**2
space_mesh = int(1/h)+1
time_mesh = 3

# tri-diagonal matrix
left_tri = np.diag([1+r+r*h]+[1+r]*2+[1+r+r*h], k=0) + \
    np.diag([-r]+2*[-r/2], k=1) + np.diag([-r/2]*2+[-r], k=-1)
right_tri = np.diag([1-r-r*h]+[1-r]*2+[1-r-r*h], k=0) + \
    np.diag([r]+2*[r/2], k=1) + np.diag([r/2]*2+[r], k=-1)

print(left_tri)
print(right_tri)
# matrix filling initial condition
u = np.zeros((time_mesh, space_mesh))

for i in range(space_mesh):
    u[0, i] = 1

print(u)
print('_'*100)
for n in range(1, time_mesh):
    rhs = np.dot(right_tri, u[n-1])
    u[n] = np.linalg.solve(left_tri, rhs.T)

print(u)
