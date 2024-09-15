import sys
from time import perf_counter
from collections import deque

start_state = ".xxxxxxxxxxxxxx"
goal_state = "x.............."
all_moves = [(0,1,3), (0,2,5), (1, 3, 6), (1, 4, 8), (2, 4, 7), (2, 5, 9), (3, 4, 5), (3, 6, 10), (3, 7, 12), (4, 7, 11), (4,8,13), (5, 8, 12), (5, 9, 14), (6, 7, 8), (7, 8, 9), (10, 11, 12), (11, 12, 13), (12, 13, 14)]

def swap(original, first, second, removal):
    lst_of_characters = list(original)
    lst_of_characters[int(first)], lst_of_characters[int(second)] = lst_of_characters[int(second)], lst_of_characters[int(first)]
    lst_of_characters[removal] = "."
    return "".join(lst_of_characters)

def get_children(state):
    children = list()
    for x in all_moves:
        if state[x[0]] == "x" and state[x[1]] == "x" and state[x[2]] == ".":
            children.append(swap(state, x[0], x[2],x[1]))
        if state[x[2]] == "x" and state[x[1]] == "x" and state[x[0]] == ".":
            children.append(swap(state, x[0], x[2],x[1]))
    return children

def DFS(start):
    fringe = deque()
    visited = set()
    paren_dict = dict()
    fringe.append(start)
    visited.add(start)
    paren_dict[start] = None
    while fringe:
        temp = fringe.pop()
        if temp == goal_state:
            lst_of_moves = list()
            g = temp
            lst_of_moves.append(g)
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            return (lst_of_moves, len(lst_of_moves))
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    return (list(), None)


def BFS(start):
    fringe = deque()
    visited = set()
    paren_dict = dict()
    fringe.append(start)
    visited.add(start)
    paren_dict[start] = None
    while fringe:
        temp = fringe.popleft()
        if temp == goal_state:
            lst_of_moves = list()
            g = temp
            lst_of_moves.append(g)
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            return (lst_of_moves, len(lst_of_moves))
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    return (list(), None)

def print_puzzle(board):
    toRet = "    " + board[0] + "    " + "\n" + "   " + board[1] + " " + board[2] + "   " + "\n" + "  " + board[3] + " " + board[4] + " " + board[5] + "  " + "\n" + " " + board[6] + " " + board[7] + " " + board[8] + " " + board[9] + " " + "\n" + board[10] + " " + board[11] + " " + board[12] + " " + board[13] + " " + board[14]
    return toRet

bfs_path, bfs_length = BFS(start_state)
dfs_path, dfs_length = DFS(start_state)

print("BFS:")
for board_state in reversed(bfs_path):
    print(print_puzzle(board_state))
    print()

print(bfs_length)
print()
print("DFS:")
for board_state2 in reversed(dfs_path):
    print(print_puzzle(board_state2))
    print()

print(dfs_length)
