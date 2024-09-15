import math
import sys
import ast

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


def XOR(i1, i2):
    #XOR Happens Here!
    p3 = perceptron(step, (1,1), -0.5, (i1, i2))
    p4 = perceptron(step, (-1,-2), 3, (i1,i2))
    return perceptron(step, (1,1), -1.5, (p3, p4))


truth_table_model = {
    (-1, 0) : 1,
    (0, -1) : 0,
    (0, 1) : 1, 
    (1, 0) : 0
}

#print(pretty_print_tt(truth_table_model))
#model_perceptron(truth_table(2, 1), 2)
            
#print(check(ast.literal_eval(sys.argv[1]), ast.literal_eval(sys.argv[2]), ast.literal_eval(sys.argv[3])))
#print(pretty_print_tt(truth_table(4, 32768)))
#w,b = model_perceptron(truth_table_model, 2)
#print(w,b)
#print(w, b, check(int(sys.argv[2]), w,b))

#print(test_perfect_functions(4))

tup = ast.literal_eval(sys.argv[1])
print(XOR(tup[0], tup[1]))