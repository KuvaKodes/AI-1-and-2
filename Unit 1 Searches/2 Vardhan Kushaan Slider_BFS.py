from collections import deque
import sys
from time import perf_counter

with open("slide_puzzle_tests.txt")as f:
    line_list = [line.strip().split() for line in f]

def print_puzzle(size, state):
    finstring = str()
    count = 0
    for z in range(0,int(size)**2):
        count = count + 1
        finstring = finstring + state[z] + " "
        if count % int(size) == 0:
            finstring = finstring + "\n"
    return(finstring)

def find_goal(state):
    return "".join((sorted(str(state.replace(".",""))))) + "."

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

def BFS(start):
    goal_state = find_goal(start)
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
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            return lst_of_moves
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    return None

def all_BFS(start):
    fringe = deque()
    visited = set()
    fringe.append(start)
    visited.add(start)
    while fringe:
        temp = fringe.popleft()
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
    return visited

def isValid(test):
    fullSet = all_BFS("12345678.")
    if test in fullSet:
        return True
    else:
        return False

def ten_moves_BFS(start):
    fringe = deque()
    visited = set()
    paren_dict = dict()
    visited_dict = dict()
    toRet = list()
    fringe.append(start)
    visited.add(start)
    paren_dict[start] = None
    while fringe:
        temp = fringe.popleft()
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    for x in visited: 
            lst_of_moves = list()
            g = x
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            visited_dict[x] = len(lst_of_moves)
    for n in visited_dict:
        if visited_dict[n] == 10:
            toRet.append(n)
    return len(toRet)

def hardest_possible_BFS(start):
    fringe = deque()
    visited = set()
    paren_dict = dict()
    visited_dict = dict()
    fringe.append(start)
    visited.add(start)
    paren_dict[start] = None
    toRet = list()
    retList = list()
    while fringe:
        temp = fringe.popleft()
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    for x in visited: 
            lst_of_moves = list()
            g = x
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            visited_dict[x] = len(lst_of_moves)
    for n in visited_dict:
        if visited_dict[n] == 31:
            toRet.append(n)
    for b in toRet:
        retList.append([b, BFS(b), visited_dict[b]])
    return retList
           
print(hardest_possible_BFS("12345678."))
""" for i in range(len(line_list)):
    start = perf_counter()
    print("Line %s: %s, %s moves found in %s" % (i, line_list[i][1], BFS(line_list[i][1]), (perf_counter()-start)))
 """ 
