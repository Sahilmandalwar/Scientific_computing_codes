def func(x,y):
    return x**2 + y**2

def second_derivative(x,y):
    return 2*x + 2*y*func(x,y)

def third_derivative(x,y):
    return 2 + 2*((func(x,y)**2) + y*second_derivative(x,y))

def fourth_derivative(x,y):
    return 2*((2*(func(x,y)*second_derivative(x,y))) + func(x,y)*second_derivative(x,y) + y*third_derivative(x,y))


h = 0.1
find_x = 0.5


def taylor_fourth(y, x, h):
    return y + h*func(x, y) + h**2 / 2 * second_derivative(x, y) + h**3 / 6 * third_derivative(x, y) + h**4 / 24 * fourth_derivative(x, y)


def adam_bashwart_formula(fun_val, h):
    return h/24 * (55*fun_val[-1] - 59*fun_val[-2] + 37*fun_val[-3] - 9*fun_val[-4])


def adam_bashwart_method(h, x, y):
    fun_val = []
    new_y_val = []
    # initially x is zero
    for i in range(4):   # compute initial four value for adam_bashwart fourth order
        f_val = func(x, y)   # first x = 0 is consider
        fun_val.append(f_val)    # first f_0 value is found
        new_y_val.append(y)
        # y = euler_method(y,x,h) # y_1 is calculated
        y = taylor_fourth( y, x, h)
        x += h                  # x_1 is calculated

    # starting from x = 0 we arrived till x = 2
    # value of x is incremented to x = 3
    while x <= find_x:
        y = new_y_val[-1] + adam_bashwart_formula(fun_val, h)
        f_val = func(x, y)
        fun_val.append(f_val)
        new_y_val.append(y)
        x += h

    return new_y_val[-1]


print(f"value of y({find_x}) : ", adam_bashwart_method(h, 0, 1))
