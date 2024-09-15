import sys
import ast
import numpy as np
import math

def A(n): 
    return 1 / (1 + np.e**-n)
new_A = np.vectorize(A)

def back_propogate(A_vec, weights, biases, training_set, epochs):
    l = 0.2
    for epoch in range(epochs):
        error_list = list()
        for input, actual_output in training_set:
            a = list() 
            a.append(input)
            for layer in range(1, len(weights)):
                a.append(A_vec((weights[layer]@a[layer-1])+biases[layer]))
            error_list.append(0.5 * ((np.sum(np.square((actual_output - a[len(weights)-1])))) ** 0.5))
            delta_lists = [None] * len(weights)
            delta_lists[len(weights)-1] = (a[len(weights)-1] * (1 - a[len(weights)-1])) * (actual_output - a[len(weights)-1])
            for layer in range(len(weights)-2, 0, -1):
                delta_lists[layer] = (a[layer] * (1-a[layer])) * (weights[layer+1].T @ delta_lists[layer+1])
            for layer in range(1,len(weights)):
                weights[layer] = weights[layer] + (l * (delta_lists[layer] @ a[layer-1].T))
                biases[layer] = biases[layer] + (l*delta_lists[layer])
        l = sum(error_list)/len(error_list)
    return weights, biases

def back_propogate_sum(A_vec, weights, biases, training_set, epochs):
    for epoch in range(epochs):
        for input, actual_output in training_set:
            a = list() 
            a.append(input)
            for layer in range(1, len(weights)):
                a.append(A_vec((weights[layer]@a[layer-1])+biases[layer]))
            delta_lists = [None] * len(weights)
            delta_lists[len(weights)-1] = (a[len(weights)-1] * (1 - a[len(weights)-1])) * (actual_output - a[len(weights)-1])
            for layer in range(len(weights)-2, 0, -1):
                delta_lists[layer] = (a[layer] * (1-a[layer])) * (weights[layer+1].T @ delta_lists[layer+1])
            for layer in range(1,len(weights)):
                weights[layer] = weights[layer] + (0.1 * (delta_lists[layer] @ a[layer-1].T))
                biases[layer] = biases[layer] + (0.1*delta_lists[layer])
            print(a[len(weights)-1])
    return weights, biases

def back_propogate_circle(A_vec, weights, biases, training_set, epochs):
    l = 0.2
    for epoch in range(epochs):
        error_list = list()
        for input, actual_output in training_set:
            a = list() 
            a.append(input)
            for layer in range(1, len(weights)):
                a.append(A_vec((weights[layer]@a[layer-1])+biases[layer]))
            error = 0.5 * ((np.sum(np.square((actual_output - a[len(weights)-1])))) ** 0.5)
            error_list.append(error)
            delta_lists = [None] * len(weights)
            delta_lists[len(weights)-1] = (a[len(weights)-1] * (1 - a[len(weights)-1])) * (actual_output - a[len(weights)-1])
            for layer in range(len(weights)-2, 0, -1):
                delta_lists[layer] = (a[layer] * (1-a[layer])) * (weights[layer+1].T @ delta_lists[layer+1])
            for layer in range(1,len(weights)):
                weights[layer] = weights[layer] + (l * (delta_lists[layer] @ a[layer-1].T))
                biases[layer] = biases[layer] + (l*delta_lists[layer])
        l = sum(error_list)/len(error_list)
        print(epoch, test_circle(A_vec, weights, biases, training_set))
    return weights, biases

def test_circle(A_vec, weights, biases, training_set):
    num_inaccurate = 0
    for input, output in training_set:
        in_or_out = output[0,0]
        if p_net(A_vec, weights, biases, input)[0,0] > 0.5:
            final_output = 1
        else:
            final_output = 0
        if in_or_out != final_output:
            num_inaccurate += 1
    return num_inaccurate

def p_net(A_vec, weights, biases, inputs):
    a = list()
    a.append(inputs)
    for layer in range(1, len(weights)):
        a.append(A_vec((weights[layer]@a[layer-1])+biases[layer]))
    return a[len(weights)-1]

if sys.argv[1] == "S":
    sum_table = [(np.array([[0], [0]]), np.array([[0], [0]])), (np.array([[0], [1]]), np.array([[0], [1]])), (np.array([[1], [0]]), np.array([[0], [1]])), (np.array([[1], [1]]), np.array([[1], [0]]))]
    sum_random_biases = [None, np.array([[np.random.uniform(-1,1)], [np.random.uniform(-1,1)]]), np.array([[np.random.uniform(-1,1)], [np.random.uniform(-1,1)]])]
    sum_random_weights = [None, np.array([[np.random.uniform(-1,1), np.random.uniform(-1,1)], [np.random.uniform(-1,1), np.random.uniform(-1,1)]]), np.array([[np.random.uniform(-1,1), np.random.uniform(-1,1)], [np.random.uniform(-1,1), np.random.uniform(-1,1)]])]
    w, b = back_propogate_sum(new_A, sum_random_weights, sum_random_biases, sum_table, 10000)


if sys.argv[1] == "C":
    circle_table = list()
    with open("10000_pairs.txt") as f: 
        for line in f:
            string_input = line.strip().split()
            input_vector = (ast.literal_eval(string_input[0]), ast.literal_eval(string_input[1]))
            quick_maths = (((input_vector[0]**2)+(input_vector[1]**2))**0.5)
            output = 0
            if quick_maths < 1:
                output = 1 
            circle_table.append((np.array([[input_vector[0]],[input_vector[1]]]), np.array([[output]])))
    circle_random_weights = [None, 2 * np.random.rand(12, 2) - 1, 2 * np.random.rand(4, 12) - 1, 2 * np.random.rand(1, 4) - 1]
    circle_random_biases = [None, 2 * np.random.rand(12, 1) - 1, 2 * np.random.rand(4, 1) - 1, 2 * np.random.rand(1, 1) - 1]
    #circle_random_weights = [None, np.zeros((12, 2)), np.zeros((4, 12)), np.zeros((1, 4))]
    #circle_random_biases = [None, np.zeros((12, 1)), np.zeros((4, 1)), np.zeros((1, 1))]
    w, b = back_propogate_circle(new_A, circle_random_weights, circle_random_biases, circle_table, 10000)
