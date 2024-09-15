import sys
import numpy as np
import ast
import math
import matplotlib.pyplot as plt

possible_inputs = list()

def truth_table(bits, n):
    truth_dictionary = dict()
    num = 2**bits
    output_string  = bin(n)[2:].zfill(num)
    possible_values(bits, [None] * bits, 0)
    for index,input in enumerate(reversed(possible_inputs)):
        truth_dictionary[input] = output_string[index]
    possible_inputs.clear()
    return truth_dictionary

    
def external_handler(list):
    input_tuple = tuple(list.copy())
    possible_inputs.append(input_tuple)
    return

def possible_values(bits, output, i):
    if i == bits:
        external_handler(output)
        return
    output[i] = 0
    possible_values(bits, output, i + 1)
    output[i] = 1
    possible_values(bits, output, i + 1)

def pretty_print_tt(table):
    output = ""
    for key, value in table.items():
        for i in key: 
            output += str(i) + "\t" 
        output += "|\t"
        output += str(value)
        output += "\n"
    return(output)

def step(num):
    if num > 0: 
        return 1
    return 0

def perceptron(A, w, b, x):
    single_vector = list()
    for index, value in enumerate(w):
        single_vector.append(value * x[index])
    return A(sum(single_vector) + b)

def check(n, w, b):
    total = 0
    truth_dict = truth_table(len(w), n)
    for key, value in truth_dict.items():
        if perceptron(step, w, b, key) == int(value):
            total += 1
    return total/(2**len(w))

def test_perfect_functions(bits): 
    total_perfects = 0
    for truth_possib in range(2 ** 2 ** bits):
        truth_dict = truth_table(bits, truth_possib)
        w, b = model_perceptron(truth_dict, bits)
        accuracy = check(truth_possib, w, b)
        if accuracy == 1:
            total_perfects = total_perfects + 1
    return total_perfects

def model_perceptron(table, bits):
    w = tuple([0 for i in range(bits)])
    b = 0
    for epoch in range(100):
        previous_epoch_w = w
        previous_epoch_b = b
        for key, value in table.items():
            f_star = perceptron(step, w, b, key)
            f_x = int(value)
            if f_star != f_x:
                new_w = list()
                for index, vector_value in enumerate(w):
                    new_w.append(vector_value + ((f_x - f_star) * key[index]))
                w = tuple(new_w)
                b = b + (f_x - f_star)
        if (w == previous_epoch_w) and (b == previous_epoch_b):
            break
    return(w, b)

fig, axs = plt.subplots(4,4)
for two_bit in range(16):
    axs[two_bit%4, two_bit//4].plot(-2,-2)
    axs[two_bit%4, two_bit//4].plot(-2,2)
    axs[two_bit%4, two_bit//4].plot(2,-2)
    axs[two_bit%4, two_bit//4].plot(2,2)
    truth_dict = truth_table(2,two_bit)
    for i in np.arange(-2,2,0.1):
        for j in np.arange(-2,2,0.1):
            if perceptron(step, model_perceptron(truth_dict, 2)[0], model_perceptron(truth_dict, 2)[1], (i,j)) > 0.5:
                axs[two_bit//4, two_bit%4].plot(i, j, color="c", linewidth= 5, marker = ".")
            else:
                axs[two_bit//4, two_bit%4].plot(i, j, color="m", linewidth= 5, marker = ".")
    for key in truth_dict.keys():
        x, y = key
        if truth_dict[key] == "1":
            axs[two_bit//4, two_bit%4].plot(x, y, color="green", linewidth= 50, marker = ".")
        else:
            axs[two_bit//4, two_bit%4].plot(x, y, color="red", linewidth= 50, marker = ".")

plt.show()