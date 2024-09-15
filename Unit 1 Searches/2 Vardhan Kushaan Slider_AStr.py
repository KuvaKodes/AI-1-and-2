import sys
from time import perf_counter
import heapq

with open(sys.argv[1])as f:
    line_list = [line.strip().split() for line in f]

def swap(original, first, second):
    lst_of_characters = list(original)
    lst_of_characters[int(first)], lst_of_characters[int(second)] = lst_of_characters[int(second)], lst_of_characters[int(first)]
    return "".join(lst_of_characters)


def get_children(start_state):
    possible_moves = list()
    size = len(start_state) ** 0.5
    space = start_state.find(".")
    if space % size == 0:
        possible_moves.append(swap(start_state, space, space+1))
    elif space % size == size-1: 
        possible_moves.append(swap(start_state, space, space-1))
    else: 
        possible_moves.append(swap(start_state, space, space+1))
        possible_moves.append(swap(start_state, space, space-1))
    if space//size == 0:
        possible_moves.append(swap(start_state, space, space+size))
    elif space//size == size-1: 
        possible_moves.append(swap(start_state, space, space-size))
    else:
        possible_moves.append(swap(start_state, space, space+size))
        possible_moves.append(swap(start_state, space, space-size))
    return possible_moves

def parity_check(board):
    rows = len(board) ** 0.5
    unordered_counter = 0
    new_board = board.replace(".", "")
    for index, value in enumerate(new_board):
        for val in new_board[:index]:
            if val > value: 
                unordered_counter = unordered_counter + 1
    if rows % 2 == 1:
        if unordered_counter % 2 == 0:
            return True
        else:
            return False
    else: 
        row_num = (board.find("."))//rows
        if row_num % 2 == 0 and unordered_counter % 2 == 1:
            return True
        elif row_num % 2 == 1 and unordered_counter % 2 == 0:
            return True
        else:
            return False

def taxicab(board):
    size = len(board) ** 0.5
    horizontal_total = 0
    vertical_total = 0 
    goal_board = "".join(sorted(board.replace(".", ""))) + "."
    for ind, val in enumerate(board):
        if val == ".":
            continue
        else: 
            vertical_total = vertical_total + abs(((ind//size)-(goal_board.find(val)//size)))
            horizontal_total = horizontal_total + abs((ind % size)-(goal_board.find(val) % size))
    return horizontal_total + vertical_total

def a_str1(board):
    closed = set()
    goal_board = "".join(sorted(board.replace(".", ""))) + "."
    paren_dict = dict()
    fringe = list()
    fringe.append((taxicab(board), board, 0))
    heapq.heapify(fringe)
    paren_dict[board] = None
    while fringe: 
        temp_heuristic, temp_state, temp_depth = heapq.heappop(fringe)
        if temp_state == goal_board: 
            lst_of_moves = list()
            g = temp_state
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            return len(lst_of_moves)
        if temp_state not in closed: 
            closed.add(temp_state)
            for child in get_children(temp_state):
                if child not in closed:
                    heapq.heappush(fringe, ((temp_depth + 1 + taxicab(child), child, temp_depth + 1)))
                    paren_dict[child] = temp_state


def a_str(board):
    closed = set()
    goal_board = "".join(sorted(board.replace(".", ""))) + "."
    fringe = list()
    fringe.append((taxicab(board), board, 0))
    heapq.heapify(fringe)
    while fringe: 
        temp_heuristic, temp_state, temp_depth = heapq.heappop(fringe)
        if temp_state == goal_board: 
            return temp_depth
        if temp_state not in closed: 
            closed.add(temp_state)
            for child in get_children(temp_state):
                if child not in closed:
                    heapq.heappush(fringe, ((temp_depth + 1 + taxicab(child), child, temp_depth + 1)))

for ind, val in enumerate(line_list):
    start = perf_counter()
    if(parity_check(val[1])):
        print(f"Line {ind}: {val[1]}, A* - {a_str(val[1])} moves in {perf_counter() - start} seconds")
    else:
        print(f"Line {ind}: {val[1]}, no solution determined in {perf_counter() - start} seconds")
