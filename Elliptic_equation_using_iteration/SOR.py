# i am using gauss seidal here

import numpy as np
import math

h = 1/3
space_step = int(1/h) + 1
u_init = np.zeros((space_step, space_step))
max_iter = 16
max_tollerence = 1e-3
omega = 1.1


def boundry_initial_condition(u):
    u[:, 0] = 0
    u[:, -1] = 0
    u[0, :] = 0
    u[1:-1, -1] = 12.4


boundry_initial_condition(u_init)
for iter in range(max_iter):
    u = u_init.copy()
    for i in range(1, space_step-1):
        for j in range(1, space_step-1):
            u_init[i,j] = 0.25*(u_init[i+1, j] + u_init[i,j+1] + u_init[i-1, j] + u_init[i, j-1])
            u_init[i,j] = (1-omega)*u[i,j] + omega*(u_init[i,j])
    error = np.max(np.abs(u_init - u))
    if (error <= max_tollerence):
        print(f'tollerence acheived and iteration required: {iter}')
        break

print(u_init)
