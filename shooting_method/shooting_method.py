
# import math
# import sympy as sp
# # y`` = y + 1 y(0) = 0 y(1) = e - 1
# # y`` = y - 4*x*e**x
# h = 0.25

# def fun_y(x,y,z):
#     return z

# def fun_z(x,y,z):
#     return y + 1

# def matrix_transform(x,y,z):
#     return sp.Matrix([[fun_y(x,y,z)],[fun_z(x,y,z)]])


# def get_val(x,y,z):

#     k1 = h * (matrix_transform(x,y,z))
#     k2 = h * (matrix_transform(x + h/2 , y + k1[0]/2 , z + k1[1]/2 ))
#     k3 = h * (matrix_transform(x + h/2 , y + k2[0]/2, z + k2[1]/2))
#     k4 = h * (matrix_transform(x + h , y + k3[0] , z + k3[1]))



#     return matrix_transform(x,y,z) 

# y_1 = get_val(0,0, 1)
# y_2 = get_val(0,-1, 0)

# def get_lambda(actual_y, y_1, y_2):
#     return (actual_y - y_2) / (y_1 - y_2)

# print(get_lambda(math.e - 1, y_1, y_2))

print("Hello")

import math
import sympy as sp

h = 0.25

def fun_y(x,y,z):
    return z

def fun_z(x,y,z):
    return y + 1

def matrix_transform(x,y,z):
    return sp.Matrix([[fun_y(x,y,z)], [fun_z(x,y,z)]])

def rk4_solve(x0, y0, z0, x_end):
    """Solve system from x0 to x_end with step h"""
    Y = sp.Matrix([[y0],[z0]])
    x = x0
    while x < x_end:
        k1 = h * matrix_transform(x, Y[0], Y[1])
        k2 = h * matrix_transform(x + h/2, Y[0] + k1[0]/2, Y[1] + k1[1]/2)
        k3 = h * matrix_transform(x + h/2, Y[0] + k2[0]/2, Y[1] + k2[1]/2)
        k4 = h * matrix_transform(x + h,   Y[0] + k3[0],   Y[1] + k3[1])
        Y = Y + (k1 + 2*k2 + 2*k3 + k4)/6
        x += h
    return Y  # final [y,z] at x_end

# Two trial initial slopes
Y1 = rk4_solve(0, 0, 1, 1)
Y2 = rk4_solve(0, 0, 0, 1)

def get_lambda(actual_y, y1, y2):
    return (actual_y - y2[0]) / (y1[0] - y2[0])

lam = get_lambda(math.e - 1, Y1, Y2)
print("λ =", lam)
