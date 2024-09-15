import numpy as np
import sys
import math
import ast

#xor
def step(x): 
    if x > 0:
        return 1
    else:
        return 0 

weights = [None, np.array([[1, 1], [-1, -2]]), np.array([[1, 1]])]
biases = [None, np.array([[-0.5],[3]]), np.array([[-1.5]])]

def p_net(A_vec, weights, biases, inputs):
    a = list()
    a.append(inputs)
    for layer in range(1, len(weights)):
        a.append(A_vec((weights[layer]@a[layer-1])+biases[layer]))
    return a[len(weights)-1]

#print(p_net(new_A, weights, biases, np.array([[1],[1]])))

#DIAMOND 

weights_diamond = [None, np.array([[1,1],[1,-1],[-1,-1],[-1,1]]), np.array([[1,1,1,1]])]
biases_diamond = [None, np.array([[1],[1],[1],[1]]), np.array([[-3.5]])]

#print(p_net(new_A, weights_diamond, biases_diamond, np.array([[-0.23],[0.76]])))

#CIRCLE 

def A(n): 
    return 1 / (1 + np.e**n)
new_A = np.vectorize(A)

def test_circle(A_vec, weights, biases):
    accuracy = 0
    inaccurate_list = list()
    for input in range(500):
        input_array = np.array([[np.random.uniform(-1,1)],[np.random.uniform(-1,1)]])
        if ((((input_array[0,0]**2)+(input_array[1,0]**2))**0.5) < 1): 
            in_or_out = 1
        else:
            in_or_out = 0
        final_output = round(np.sum(np.square(p_net(A_vec, weights, biases, input_array))) ** 0.5)
        if in_or_out == final_output:
            accuracy += 1
        else:
            inaccurate_list.append((input_array[0,0],input_array[1,0]))
    return inaccurate_list, accuracy/5

biases_circle = [None, np.array([[1.05],[1.05],[1.05],[1.05]]), np.array([[-1.2]])]

#print(test_circle(new_A, weights_diamond, biases_circle))

if len(sys.argv) == 1:
    print(test_circle(new_A, weights_diamond, biases_circle))
elif len(sys.argv) == 2:
     #XOR HAPPENS HERE
     input_tuple = ast.literal_eval(sys.argv[1])
     print(p_net(np.vectorize(step), weights, biases, np.array([[input_tuple[0]],[input_tuple[1]]])))
else: 
    print(p_net(np.vectorize(step), weights_diamond, biases_diamond, np.array([[ast.literal_eval(sys.argv[1])],[ast.literal_eval(sys.argv[2])]])))

    
