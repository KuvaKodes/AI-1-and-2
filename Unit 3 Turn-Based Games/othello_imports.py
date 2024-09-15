import sys

blank_board = "...........................ox......xo..........................."

def convert_10_to_8(index):
    row = index//10
    col = index % 10
    return(row-1)*8 + (col-1)

def convert_8_to_10(index):
    row = index//8
    col = index % 8
    return (row+1)*10 + (col+1)

def print_board(board):
    new_board = ""
    for i in range(0,8):
        new_board = new_board + board[i*8:i*8 + 8] + "\n"
    return new_board

def convert_board(board):
    new_board = "??????????" 
    for i in range(0, 8):
        new_board = new_board + "?" + board[(i*8):(i*8) + 8] + "?"
    new_board = new_board + "??????????"
    return new_board
    

def possible_moves(board,token):
    board = convert_board(board)
    opponent = "xo"["ox".index(token)]
    directions = [-11,-10,-9,-1,1,9,10,11]
    current_locations = list()
    legal_moves = set()
    for ind, val in enumerate(board):
        if val == token:
            current_locations.append(ind)
    for start in current_locations:
        for direction in directions:
            next_ind = start+direction
            if board[next_ind] == opponent:
                while board[next_ind] == opponent:
                    next_ind = next_ind + direction
                if board[next_ind] == ".":
                    legal_moves.add(convert_10_to_8(next_ind))
    return list(legal_moves)

def make_move(board, token, index):
    board = convert_board(board)
    index = convert_8_to_10(index)
    opponent = "xo"["ox".index(token)]
    directions = [-11,-10,-9,-1,1,9,10,11]
    valid_directions = list()
    new_board = board[0:index] + token + board[index+1:]
    for direction in directions:
        next_ind = index + direction
        if board[next_ind] == opponent:
            while board[next_ind] == opponent:
                next_ind = next_ind + direction
            if board[next_ind] == token:
                valid_directions.append(direction)
    for direction in valid_directions:
        next_ind = index + direction
        while board[next_ind] != token:
            new_board = new_board[:next_ind] + token + new_board[next_ind+1:]
            next_ind = next_ind + direction
    return new_board.replace("?","")


        
            
            

