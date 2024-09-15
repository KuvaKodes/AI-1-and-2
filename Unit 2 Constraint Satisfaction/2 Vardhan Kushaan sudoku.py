import random
import sys
from time import perf_counter

with open(sys.argv[1]) as f:
    board_list = [line.strip() for line in f]

def display_board(board):
    toRet = ""
    for j in range(size):
        if j != 0 and j % subblock_height == 0:
            toRet = toRet + ("- " * int((size*2-sublock_width))) + "\n"
        for i in range(size):
            if i!= 0 and i % sublock_width == 0:
                toRet = toRet + "| "
            toRet = toRet + board[i+(j*size)] + "  "
        toRet = toRet + "\n"
    return toRet


def get_constraints(board):
    list_of_constraint_sets = list()
    for j in range(size):
        row_set = set()
        for i in range(size):
            row_set.add(i+(j*size))
        list_of_constraint_sets.append(row_set)

    for j in range(size):
        col_set = set()
        for i in range(size):
            col_set.add(j + (i*size))
        list_of_constraint_sets.append(col_set)

    for n_width in range(subblock_height):
        for n_height in range(sublock_width):
            block_set = set()
            top_left = (n_width*sublock_width) + (n_height*subblock_height) + (n_height*subblock_height*(size-1))
            for j in range(subblock_height):
                for i in range(sublock_width):
                    block_set.add(top_left + (i + (j*size)))
            list_of_constraint_sets.append(block_set)

    return list_of_constraint_sets

def gut_check(board):
    for val in board:
        if len(board[val]) > 1:
            return False
    for i in symbol_set:
        count_per_var = 0
        for val in list(board.values()):
            if val == i:
                count_per_var = count_per_var + 1
        if count_per_var != size:
            return False
    return True

def get_sorted_values(board, var):
    list_of_possible_values = list(symbol_set)
    for index_of_restriction in constrainers[var]:
        if board[index_of_restriction] in list_of_possible_values:
            list_of_possible_values.remove(board[index_of_restriction])
    return list_of_possible_values

def forward_looking(board, newly_solved_indices):
    for index in newly_solved_indices:
        for constraint in constrainers[index]:
            if board[index] in board[constraint]:
                board[constraint] = board[constraint].replace(board[index],"")
                if not board[constraint]:
                    return None
                if len(board[constraint]) == 1:
                    newly_solved_indices.append(constraint)
    return board

def get_most_constrained_var(board):
    min  = float('inf')
    options = list()
    for indy in range(len(board)):
        if len(board[indy]) > 1 and len(board[indy]) < min:
            min = len(board[indy])
    for indy in range(len(board)):
        if len(board[indy]) == min:
            options.append(indy)
    return random.choice(options)

def csp_backtracking(board):
    if gut_check(board): 
        return board
    var = get_most_constrained_var(board)
    for val in board[var]:
        new_board = {i:board[i] for i in range(len(board))}
        new_board[var] = val
        checked_board = forward_looking(new_board, [var,])
        if checked_board is not None:
            result = csp_backtracking(checked_board)
            if result is not None:
                return result
    return None

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in board_list:
    state = x
    if (len(state) ** 0.25) == int(len(state)**0.25):
        size = int(len(state) ** 0.5)
        subblock_height = sublock_width = int(len(state) ** 0.25)
    else: 
        size = int(len(state) ** 0.5)
        factor_list = list()
        for i in range(1, int(size**0.5)+1):
            if size % i == 0:
                factor_list.append(i)
                factor_list.append(int(size/i))
                factor_list = sorted(factor_list)
        for g in factor_list:
            if g > int(size**0.5):
                sublock_width = g
                subblock_height = size//g
                break
    if size <= 9:
        symbol_set = {str(i) for i in range(1, size+1)}
    else:
        symbol_set = {str(i) for i in range(1, 10)}
        for j in range(size-9):
            symbol_set.add(alphabet[j])
    constrainers = dict()
    list_of_constraint_sets = get_constraints(x)
    for square in range(len(state)):
        constrainers[square] = set()
        for constraints in list_of_constraint_sets:
            if square in constraints: 
                for ind in constraints:
                    if ind != square:
                        constrainers[square].add(ind)
               
    next_state = dict()
    for i in range(len(state)):
        if state[i] != ".":
            next_state[i] = state[i]
        else:
            next_state[i] = "".join(get_sorted_values(state, i))

    print("".join(csp_backtracking(next_state).values()))


