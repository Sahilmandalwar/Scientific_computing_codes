import numpy as np
import math


h = 1/3
space_step = int(1/h) + 1
max_tollerence = 1e-2
u_init = np.zeros((space_step, space_step))
max_iter = 3

def boundry_initial_condition(u):
    for i in range(space_step):
        u[0,i] = 0
        u[space_step - 1,i] = 0
        u[i,0] = 0
    for i in range(1,space_step-1):
        u[i,space_step-1] = 12.4

boundry_initial_condition(u_init)  # we have k values here
for _ in range(max_iter):
    u_new = np.zeros((space_step,space_step))
    boundry_initial_condition(u_new)
    for i in range(1, space_step - 1):
        for j in range(1, space_step-1):
            u_new[i,j] = 0.25*(u_init[i-1,j] + u_init[i+1,j] + u_init[i,j-1] + u_init[i,j+1])
    error = np.max(np.abs(u_new - u_init))
    print(u_init)
    if(error <= max_tollerence):
        print("tollerence acheived")
        break
    u_init = u_new

print(u_init)


