import random
from time import perf_counter


def initial_board(size):
    return (board := [None for x in range(size)])

def get_next_unassigned_var(board):
    if None not in board:
        return None
    i = int((len(board)//2))
    val = board[i]
    while val is not None: 
        i = random.randint(0, len(board)-1)
        val = board[i]
    return i 

def check_diags(board, test, start):
        step_counter = 0
        for back in board[start::-1]:
            if back == test - step_counter or back == test + step_counter:
                return False
            step_counter = step_counter + 1
        step_counter = 0
        for forw in board[start::]:
            if forw == test-step_counter or forw == test+step_counter:
                return False
            step_counter = step_counter+1 
        return True

def get_sorted_values(board, start):
    possible_moves = list()
    for i in range(len(board)):
        if i in board:
            continue
        if not check_diags(board, i, start):
            continue
        possible_moves.append(i)
    return possible_moves

def csp_backtracking(state):
    if None not in state: 
        return state
    var = get_next_unassigned_var(state)
    nextVals = get_sorted_values(state, var)
    for g in range(len(nextVals)):
        i = random.randint(0, len(nextVals)-1)
        val = nextVals[i]
        new_state = state.copy() 
        new_state[var] = val
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None
 
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
test_case1 = [None for x in range(33)]
test_case2 = [None for x in range(34)]
test_case3 = [None for x in range(35)]
print(ans1:= csp_backtracking(test_case1))
print(test_solution(ans1))
print(ans2:= csp_backtracking(test_case2))
print(test_solution(ans2))
print(ans3:= csp_backtracking(test_case3))
print(test_solution(ans3))
end = perf_counter()
print(end-start)

