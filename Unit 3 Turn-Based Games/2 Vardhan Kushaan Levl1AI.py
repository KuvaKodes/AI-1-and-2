import sys
import time

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

def game_over(board):
    if not possible_moves(board, "x") and not possible_moves(board, "o"):
        return True
    else:
        return False
    
def score(board):
    score = 0
    possible_moves_x = possible_moves(board, "x")
    possible_moves_o = possible_moves(board, "o")
    if not possible_moves_x and not possible_moves_o:
        count_x = board.count("x")
        count_o = board.count("o")
        if count_x > count_o:
            score = score + 1000000000000 + (count_x - count_o)
        else:
            score = score - 1000000000000 + (count_x - count_o)
    corners = [0, 7, 56, 63]
    next_to_corners = [1, 8, 9, 6, 15, 14, 48, 57, 49, 62, 55, 54]
    score = score + ((len(possible_moves_x) - len(possible_moves_o)))
    for corner in corners:
        if board[corner] == "x":
            score = score + 100
        elif board[corner] == "o":
            score = score - 100
    for square in next_to_corners:
        if board[square] == "x":
            score = score - 10 
        elif board[square] == "o":
            score = score + 10
    return score
    

def min_move(board, token, depth):
    opponent = "xo"["ox".index(token)]
    list_of_moves = possible_moves(board, token)
    results = list()
    if depth == 0 or game_over(board):
        return score(board)
    if not list_of_moves:
        return max_move(board, opponent, depth-1)
    for move in list_of_moves:
        new_board = make_move(board, token, move)
        results.append(max_move(new_board, opponent, depth-1))
    return min(results)
    

def max_move(board, token, depth):
    opponent = "xo"["ox".index(token)]
    list_of_moves = possible_moves(board, token)
    results = list()
    if depth == 0 or game_over(board):
        return score(board)
    if not list_of_moves:
        return min_move(board, opponent, depth-1)
    for move in list_of_moves:
        new_board = make_move(board, token, move)
        results.append(min_move(new_board, opponent, depth-1))
    return max(results)

def find_next_move(board, token, depth):
    opponent = "xo"["ox".index(token)]
    results = dict()
    for move in possible_moves(board, token):
        new_board = make_move(board, token, move)
        if opponent == "x":
            results[max_move(new_board, opponent, depth-1)] = move
        else:
            results[min_move(new_board, opponent, depth-1)] = move
    if token == "o":
        return results[min(results.keys())]
    else:
       return results[max(results.keys())]
        
            
            
board = sys.argv[1]
player = sys.argv[2]
depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   depth += 1

# results = []
# with open("boards_timing.txt") as f:
#     for line in f:
#         board, token = line.strip().split()
#         temp_list = [board, token]
#         print(temp_list)
#         for count in range(1, 7):
#             print("depth", count)
#             start = time.perf_counter()
#             find_next_move(board, token, count)
#             end = time.perf_counter()
#             temp_list.append(str(end - start))
#         print(temp_list)
#         print()
#         results.append(temp_list)

# with open("boards_timing_my_results.csv", "w") as g:
#     for l in results:
#         g.write(", ".join(l) + "\n")