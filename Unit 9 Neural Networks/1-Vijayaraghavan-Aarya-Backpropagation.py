import ast
import sys
import numpy as np
import random
import math

def sigmoid(n): return 1 / (1 + np.e**(-n)) 

def train(epochs, data, weights, biases, activate, alpha):
    for epoch in range(epochs):
        for datapoint in data:
            a = np.array([None, None, None])
            dotp = np.array([None, None, None])
            delta = np.array([None, None, None])

            q, z = [[datapoint[0][0], datapoint[0][1]]], [[data[datapoint][0][0], data[datapoint][0][1]]]
            x, y = np.transpose(np.asarray(q)), np.transpose(np.asarray(z))
            a[0] = x
            for layer in range(1, len(weights)):
                dotp[layer] = weights[layer].dot(a[layer - 1]) + biases[layer]
                a[layer] = activate(dotp[layer]) # activate doesn't need vectorization
            delta[len(weights) - 1] = (a[len(weights) - 1] * (1 - a[len(weights) - 1])) * (y - a[len(weights) - 1])
            for layer in range(len(weights) - 2, 0, -1):
                delta[layer] = (a[layer] * (1 - a[layer])) * (np.transpose(weights[layer + 1]).dot(delta[layer + 1]))
            for layer in range(1, len(weights)):
                weights[layer] = weights[layer] + alpha * delta[layer].dot(np.transpose(a[layer - 1]))
                biases[layer] = biases[layer] + alpha * delta[layer]
    
    return weights, biases

def test(activate, weights, biases, x):
    numlayers = len(weights)
    outputs = [0] * numlayers
    outputs[0] = np.array(x)
    for i in range(1, numlayers):
        outputs[i] = activate(weights[i] @ outputs[i - 1] + biases[i])
    return outputs[numlayers - 1]

def challenge2train(epochs, data, weights, biases, activate, alpha):
    for epoch in range(epochs):
        for datapoint in data:
            a = np.array([None, None, None])
            dotp = np.array([None, None, None])
            delta = np.array([None, None, None])

            q, z = [[datapoint[0][0], datapoint[0][1]]], [[data[datapoint][0][0], data[datapoint][0][1]]]
            x, y = np.transpose(np.asarray(q)), np.transpose(np.asarray(z))
            a[0] = x
            for layer in range(1, len(weights)):
                dotp[layer] = weights[layer].dot(a[layer - 1]) + biases[layer]
                a[layer] = activate(dotp[layer]) # activate doesn't need vectorization
            delta[len(weights) - 1] = (a[len(weights) - 1] * (1 - a[len(weights) - 1])) * (y - a[len(weights) - 1])
            for layer in range(len(weights) - 2, 0, -1):
                delta[layer] = (a[layer] * (1 - a[layer])) * (np.transpose(weights[layer + 1]).dot(delta[layer + 1]))
            for layer in range(1, len(weights)):
                weights[layer] = weights[layer] + alpha * delta[layer].dot(np.transpose(a[layer - 1]))
                biases[layer] = biases[layer] + alpha * delta[layer]
            print("Current Output:", a[2])
    
    return weights, biases

def challenge2test(activate, weights, biases, x):
    numlayers = len(weights)
    outputs = [0] * numlayers
    outputs[0] = np.transpose(np.array(x))
    for i in range(1, numlayers):
        outputs[i] = activate(weights[i] @ outputs[i - 1] + biases[i])
    
    output = outputs[numlayers - 1]
    print("Unrounded output:", output)
    for i in range(len(output)):
        if output[i] >= 0.5: output[i] = 1
        else: output[i] = 0
    return output

def challenge3train(epochs, data, weights, biases, activate, alpha):
    for epoch in range(epochs):
        for datapoint in data:
            a = np.array([None, None, None, None])
            dotp = np.array([None, None, None, None])
            delta = np.array([None, None, None, None])

            q, z = [[datapoint[0][0], datapoint[0][1]]], [[data[datapoint]]]
            x, y = np.transpose(np.asarray(q)), np.transpose(np.asarray(z))
            a[0] = x
            for layer in range(1, len(weights)):
                dotp[layer] = weights[layer].dot(a[layer - 1]) + biases[layer]
                a[layer] = activate(dotp[layer]) # activate doesn't need vectorization
            delta[len(weights) - 1] = (a[len(weights) - 1] * (1 - a[len(weights) - 1])) * (y - a[len(weights) - 1])
            for layer in range(len(weights) - 2, 0, -1):
                delta[layer] = (a[layer] * (1 - a[layer])) * (np.transpose(weights[layer + 1]).dot(delta[layer + 1]))
            for layer in range(1, len(weights)):
                weights[layer] = weights[layer] + alpha * delta[layer].dot(np.transpose(a[layer - 1]))
                biases[layer] = biases[layer] + alpha * delta[layer]

        misclassified = challenge3test(activate, weights, biases, data)
        print("Epoch:", epoch, "Misclassified:", misclassified)

# def challenge3train(epochs, data, weights, biases, activate, alpha):
#     for epoch in range(epochs):
#         for datapoint in data:
#             a = np.array([None, None, None, None])
#             dotp = np.array([None, None, None, None])
#             delta = np.array([None, None, None, None])

#             q, z = [[datapoint[0][0], datapoint[0][1]]], [[data[datapoint]]]
#             x, y = np.transpose(np.asarray(q)), np.transpose(np.asarray(z))
#             a[0] = x
#             for layer in range(1, len(weights)):
#                 dotp[layer] = weights[layer].dot(a[layer - 1]) + biases[layer]
#                 a[layer] = activate(dotp[layer]) # activate doesn't need vectorization
#             delta[len(weights) - 1] = (a[len(weights) - 1] * (1 - a[len(weights) - 1])) * (y - a[len(weights) - 1])
#             for layer in range(len(weights) - 2, 0, -1):
#                 delta[layer] = (a[layer] * (1 - a[layer])) * (np.transpose(weights[layer + 1]).dot(delta[layer + 1]))
#             for layer in range(1, len(weights)):
#                 weights[layer] = weights[layer] + alpha * delta[layer].dot(np.transpose(a[layer - 1]))
#                 biases[layer] = biases[layer] + alpha * delta[layer]

#             for i in range(1, len(delta)):
#                 print(delta[i].shape)
#             sys.exit(0)

#         misclassified = challenge3test(activate, weights, biases, data)
#         print("Epoch:", epoch, "Misclassified:", misclassified)

#     return weights, biases

def challenge3test(activate, weights, biases, x):
    misclassified = 0
    for datapoint in data:
        q, z = [[datapoint[0][0], datapoint[0][1]]], [[data[datapoint]]]
        x, y = np.transpose(np.asarray(q)), np.transpose(np.asarray(z))
        numlayers = len(weights)
        outputs = [0] * numlayers
        outputs[0] = x
        for i in range(1, numlayers):
            outputs[i] = activate(weights[i] @ outputs[i - 1] + biases[i])
        
        output = outputs[numlayers - 1]
        print(y, output)
        result = 1 if output[0][0] > 0.5 else 0
        actualresult = y[0][0]
        if result != actualresult: misclassified += 1
    return misclassified


commandarg = sys.argv[1]

if commandarg == "S":
    data = {
        ((0, 0),) : ((0, 0),),
        ((0, 1),) : ((0, 1),),
        ((1, 0),) : ((0, 1),),
        ((1, 1),) : ((1, 0),)
    }

    weights = [None, np.array([[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]]), np.array([[random.uniform(-1, 1), random.uniform(-1, 1)], [random.uniform(-1, 1), random.uniform(-1, 1)]])]
    biases = [None, np.array([[random.uniform(-1, 1)], [random.uniform(-1, 1)]]), np.array([[random.uniform(-1, 1)], [random.uniform(-1, 1)]])]

    weights, biases = challenge2train(30000, data, weights, biases, sigmoid, 0.1)

    input2 = [[1, 1]]
    output = challenge2test(sigmoid, weights, biases, input2)
    finalresult = [int(output[0][0]), int(output[1][0])]
    print("Final Output:", finalresult)

elif commandarg == "C":
    data = {}
    with open("10000_pairs.txt") as f:
        for line in f:
            vals = line.strip().split()
            x = ((float(vals[0]), float(vals[1])),)
            y = 1 if ((x[0][0] ** 2 + x[0][1] ** 2) ** 0.5) < 1 else 0
            data[x] = y
    #12x2 * 2x1
    weights = [None, 2 * np.random.rand(12, 2) - 1, 2 * np.random.rand(4, 12) - 1, 2 * np.random.rand(1, 4) - 1]    
    biases = [None, 2 * np.random.rand(12, 1) - 1, 2 * np.random.rand(4, 1) - 1, 2 * np.random.rand(1, 1) - 1]    
    print(weights, biases)
    input()
    challenge3train(200, data, weights, biases, sigmoid, 0.1)
else:
    print("Please input S or C")