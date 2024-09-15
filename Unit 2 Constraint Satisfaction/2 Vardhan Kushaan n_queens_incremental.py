import random
from time import perf_counter


def num_conflicts(board, row_num):
    tot_conf = 0
    val = board[row_num]
    for i in range(row_num):
        if board[i] == val:
            tot_conf = tot_conf +1
    for g in range(row_num+1, len(board)):
        if board[g] == val:
            tot_conf = tot_conf +1
    if row_num > 0: 
        step_counter = 1
        for back in board[row_num-1::-1]:
            if back == val - step_counter or back == val + step_counter:
                tot_conf = tot_conf +1
            step_counter = step_counter+1 
    step_counter = 1
    for forw in board[row_num+1::]:
        if forw == val - step_counter or forw == val + step_counter:
            tot_conf = tot_conf +1
        step_counter = step_counter+1
    return tot_conf

def most_conflicted_rows(board):
    most_conflicted_rows_list = list()
    row_to_conflicts = {i : num_conflicts(board, i) for i in range(len(board))}
    max = 0
    for g in row_to_conflicts: 
        if row_to_conflicts[g] > max:
            max = row_to_conflicts[g]
    for n in row_to_conflicts: 
        if row_to_conflicts[n] == max:
            most_conflicted_rows_list.append(n)
    return most_conflicted_rows_list
            
def total_conflicts(board):
    sum = 0 
    for i in range(len(board)):
        sum = sum + num_conflicts(board, i)
    return sum

def least_conflicted_squares(board, row_num):
    least_conflicted_squares_list = list()
    col_to_conflicts = {g : 0 for g in range(len(board))}
    for i in range(len(board)):
        new_board = board.copy()
        new_board[row_num] = i
        col_to_conflicts[i] = num_conflicts(new_board, row_num)
    min = 9223372036854775807
    for g in col_to_conflicts:
        if col_to_conflicts[g] < min:
            min = col_to_conflicts[g]
    for n in col_to_conflicts:
        if col_to_conflicts[n] == min:
            least_conflicted_squares_list.append(n)
    return least_conflicted_squares_list

def generate_reasonable_board(size):
    board = [random.choice(range(0,size)) for i in range(size)]
    for i in range(len(board)):
        board[i] = random.choice(least_conflicted_squares(board, i))
    return board

def inc_repair(board):
    while total_conflicts(board) != 0:
        row_to_change = random.choice(most_conflicted_rows(board))
        optimal_square = random.choice(least_conflicted_squares(board, row_to_change))
        board[row_to_change] = optimal_square
        print(board, total_conflicts(board))
    return board

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

start = perf_counter()
final1 = inc_repair(generate_reasonable_board(32))
print(test_solution(final1))
final2 = inc_repair(generate_reasonable_board(33))
print(test_solution(final2))
final3 = inc_repair(generate_reasonable_board(10_000 ))
print(test_solution(final3))
end = perf_counter()
print(end-start)