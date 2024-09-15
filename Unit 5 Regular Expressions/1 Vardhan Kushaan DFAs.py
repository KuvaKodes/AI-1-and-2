import sys

def display_dfa(dfa, alphabet):
    output = "*\t"
    for char in alphabet:
        output += "%s\t" % char
    output += "\n"
    for key in dfa.keys():
        output += "%s\t" %key
        for char in alphabet:
            if char in dfa[key].keys():
                output += "%s\t" %dfa[key][char]
            else:
                output += "_\t"
        output += "\n"
    return(output)

def traverse_dfa(input, dfa, finals):
    next_node = 0
    for char in input: 
        if char not in dfa[next_node].keys():
            return False
        else:
            next_node = dfa[next_node][char]
    if next_node in finals:
        return True
    else:
        return False


try: 
    int(sys.argv[1])
except:
    with open(sys.argv[1]) as f:
        state = f.read().split("\n\n")

    with open(sys.argv[2]) as f1:
        line_list = [line.strip() for line in f1]

    for key, val in enumerate(state):
        state[key] = val.split()

    string_finals = state[0][2:]
    final  = [int(i) for i in string_finals]

    dfa_dict = dict()
    for i in range(0, int(state[0][1])):
        dfa_dict[i] = dict()

    for i in range(1, len(state)):
        sub_state = state[i]
        for j in range(1, len(sub_state),2):
            dfa_dict[int(sub_state[0])][sub_state[j]] = int(sub_state[j+1])
 
    print(display_dfa(dfa_dict, state[0][0]))
    print("Final Nodes: %s" %final)
    for input in line_list: 
        print(traverse_dfa(input, dfa_dict, final), input)

else:
    with open(sys.argv[2]) as f1:
        line_list = [line.strip() for line in f1]
    dfa_1 = {
        0: {
            "a" : 1
        },
        1: {
            "a" : 2
        },

        2:{
            "b" : 3
        },
        3: {}
    }
    alpha_1 = "ab"
    final_1 = [3]

    dfa_2 = {
        0: {
            "1" : 1,
            "0" : 0,
            "2" : 0
        },

        1:{
            "1": 1,
            "0": 0,
            "2" : 0
        }
    }
    alpha_2 = "012"
    final_2 = [1]

    dfa_3 = {
        0: {
            "a" : 0, 
            "b" : 1,
            "c" : 0 
        },
        1: {
            "a" : 1, 
            "b" : 1,
            "c" : 1 
        }

    }
    alpha_3 = "abc"
    final_3 = [1]

    dfa_4 = {
        0: {
            "1" : 0,
            "0" : 1
        },

        1: {
            "1" : 1,
            "0" : 0
        }
    }
    alpha_4 = "01"
    final_4 = [0]

    dfa_5 = {
        0: {
            "0" : 1,
            "1" : 3
        },
        1: {
            "0" : 0,
            "1": 2
        },

        2: {
            "1": 1,
            "0": 3
        },

        3: {
            "1" : 0,
            "0": 4
        },

        4: {
            "0": 3,
            "1" : 1
        }
    }
    alpha_5 = "01"
    final_5 = [0]

    dfa_6 = {
        0: {
            "a" : 1,
            "b" : 0,
            "c" : 0
        },
        1: {
            "b" : 2,
            "a" : 1, 
            "c" : 0
        },

        2:{
            "c" : 3,
            "a" : 1,
            "b" : 0
        },
        3: {
            "c" : 3,
            "a" : 3,
            "b" : 3
        }
    }
    alpha_6 = "abc"
    final_6 = [0,1,2]

    dfa_7 = {
        0: {
            "0" : 0,
            "1" : 1
        },
        1: {
            "0" : 2,
            "1": 1
        },

        2: {
            "1": 3,
            "0": 2
        },

        3: {
            "1" : 4,
            "0": 2
        },

        4: {
            "0": 4,
            "1" : 4
        }
    }
    alpha_7 = "01"
    final_7 = [4]

    match int(sys.argv[1]):
        case 1:
            dfa_dict = dfa_1
            final = final_1
            alphabet = alpha_1
        case 2:
            dfa_dict = dfa_2
            final = final_2
            alphabet = alpha_2
        case 3:
            dfa_dict = dfa_3
            final = final_3
            alphabet = alpha_3
        case 4:
            dfa_dict = dfa_4
            final = final_4
            alphabet = alpha_4
        case 5:
            dfa_dict = dfa_5
            final = final_5
            alphabet = alpha_5
        case 6:
            dfa_dict = dfa_6
            final = final_6
            alphabet = alpha_6
        case 7:
            dfa_dict = dfa_7
            final = final_7
            alphabet = alpha_7


    print(display_dfa(dfa_dict, alphabet))
    print("Final Nodes: %s" % final)
    for input in line_list: 
        print(traverse_dfa(input, dfa_dict, final), input)