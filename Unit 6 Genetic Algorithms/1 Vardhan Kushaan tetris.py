import sys 

test = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"

piece_list = ["I0", "I1", "O0", "T0", "T1", "T2", "T3", "S0", "S1", "Z0", "Z1", "J0", "J1", "J2", "J3", "L0", "L1", "L2", "L3"]

piece_offsets = {
    "I0" : [0,0,0,0],
    "I1" : [0],
    "O0": [0,0],
    "T0" : [0,0,0],
    "T1" : [0,-1],
    "T2" : [-1,0,-1],
    "T3" : [-1,0],
    "S0" : [0,0,-1],
    "S1" : [-1,0],
    "Z0" : [-1,0,0],
    "Z1" : [0,-1],
    "J0" : [0,0,0],
    "J1" : [0,-2],
    "J2" : [-1,-1,0],
    "J3" : [0,0],
    "L0" : [0,0,0],
    "L1" : [0,0],
    "L2" : [0,-1,-1],
    "L3" : [-2,0]
}

piece_columns = {
    "I0" : [1,1,1,1],
    "I1" : [4],
    "O0": [2,2],
    "T0" : [1,2,1],
    "T1" : [3,1],
    "T2" : [1,2,1],
    "T3" : [1,3],
    "S0" : [1,2,1],
    "S1" : [2,2],
    "Z0" : [1,2,1],
    "Z1" : [2,2],
    "J0" : [2,1,1],
    "J1" : [3,1],
    "J2" : [1,1,2],
    "J3" : [1,3],
    "L0" : [1,1,2],
    "L1" : [3,1],
    "L2" : [2,1,1],
    "L3" : [1,3]
}


def column_heights(board):
    output_dict = dict()
    for col in range(10):
        col_string = ""
        for row in range(20):
            col_string += test[col + (row*10)]
        for key,value in enumerate(col_string):
            if value == "#":
                output_dict[col] = 20-key
                break
        if col not in output_dict.keys():
            output_dict[col] = 0
    return output_dict


def print_board(board):
    output = ""
    for i in range(0,len(board),10):
        output += board[i:i+10] + "\n"
    return output

def completed_row(board):
    temp = ""
    final = ""
    count = 0
    something_completed = False
    for i in range(0,len(board),10):
        if board[i:i+10] != "#"*10:
            temp += board[i:i+10]
        else:
            something_completed = True
            count += 1
    for i in range(count):
         final += " "*10
    return something_completed, final + temp


def convert(board):
    output = ""
    for char in board:
        if char == "#":
            output+= "."
        else:
            output += char
    return output

def model_game(board):
    for piece in piece_list: 
        height_dict = column_heights(board)
        for column in range(10):
            if (height_dict[column] + piece_columns[piece][0]) > 20:
                print("Game Over")
            else:
                


print(print_board(convert(test)))
print(column_heights(test))
