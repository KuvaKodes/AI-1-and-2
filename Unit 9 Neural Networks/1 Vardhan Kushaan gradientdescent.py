import sys
import numpy as np
import ast
import math


#Equation A

def function_A(x, y):
    return (4 * (x**2) ) - (3 * x * y) + (2 * (y ** 2)) + (24 * x) - (20 * y)

def x_deriv_A(x, y):
    return (8 * x) - (3 * y) + 24

def y_deriv_A(x, y):
    return (4 * y) - 20 - (3 * x)

def minimize_A():
    x = 0
    y = 0
    l = 0.1
    while (((x_deriv_A(x,y) ** 2) + (y_deriv_A(x,y) ** 2))**0.5) > (10**-8):
        new_x = x - (l * x_deriv_A(x,y))
        y = y - (l * y_deriv_A(x,y))
        x = new_x
        print(x,y, x_deriv_A(x,y), y_deriv_A(x,y))
    return x,y 


#Equation B

def function_B(x, y):
    return ((1-y) ** 2) + ((x - (y**2))**2)

def x_deriv_B(x, y):
    return 2 * (x - (y**2))

def y_deriv_B(x, y):
    return 2 * ((-2 * x * y) + (2 * (y ** 3)) + y - 1)


def minimize_B():
    x = 0
    y = 0
    l = 0.1
    while (((x_deriv_B(x,y) ** 2) + (y_deriv_B(x,y) ** 2))**0.5) > (10**-8):
        new_x = x - (l * x_deriv_B(x,y))
        y = y - (l * y_deriv_B(x,y))
        x = new_x
        print(x,y, x_deriv_B(x,y), y_deriv_B(x,y))
    return x,y 

    
if sys.argv[1] == "A":
    minimize_A()
else: 
    minimize_B()