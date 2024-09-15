import sys 
from collections import deque 
from time import perf_counter

with open(sys.argv[1])as f:
    line_list = [line.strip().split() for line in f]

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
            return len(lst_of_moves)
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    return None

def BiBFS(start):
    start_goal_state = find_goal(start)
    reverse_goal_state = start
    start_fringe = deque()
    start_visited = set()
    start_paren_dict = dict()
    reverse_fringe = deque()
    reverse_visited = set()
    reverse_paren_dict = dict() 
    start_fringe.append(start)
    start_visited.add(start)
    start_paren_dict[start] = None
    reverse_fringe.append(start_goal_state)
    reverse_visited.add(start_goal_state)
    reverse_paren_dict[start_goal_state] = None
    while start_fringe and reverse_fringe:
        start_temp = start_fringe.popleft()
        reverse_temp = reverse_fringe.popleft()
        if start_temp in reverse_visited and start_temp in start_visited: 
            lst_of_moves_forwards = list()
            lst_of_moves_backwards = list()
            forwards = start_temp
            backwards = start_temp
            while start_paren_dict[forwards]:
                forwards = start_paren_dict[forwards]
                lst_of_moves_forwards.append(forwards)
            while reverse_paren_dict[backwards]:
                backwards = reverse_paren_dict[backwards]
                lst_of_moves_backwards.append(backwards) 
            return len(lst_of_moves_backwards) + len(lst_of_moves_forwards)
        if reverse_temp in start_visited and reverse_temp in reverse_visited: 
            lst_of_moves_forw = list()
            lst_of_moves_back = list()
            forw = reverse_temp
            back = reverse_temp
            while start_paren_dict[forw]:
                forw = start_paren_dict[forw]
                lst_of_moves_forw.append(forw) 
            while reverse_paren_dict[back]:
                back = reverse_paren_dict[back]
                lst_of_moves_back.append(back)
            return len(lst_of_moves_back) + len(lst_of_moves_forw)
        for child in get_children(start_temp):
            if child not in start_visited:
                start_fringe.append(child)
                start_visited.add(child)
                start_paren_dict[child] = start_temp
        for c in get_children(reverse_temp):
            if c not in reverse_visited: 
                reverse_fringe.append(c)
                reverse_visited.add(c)
                reverse_paren_dict[c] = reverse_temp
    return None

for i in range(len(line_list)):
    #start = perf_counter()
    #print("Line %s: %s, %s moves found in %s" % (i, line_list[i][1], BFS(line_list[i][1]), (perf_counter()-start)))
    restart = perf_counter()
    print("Line %s: %s, %s moves found in %s" % (i, line_list[i][1], BiBFS(line_list[i][1]), (perf_counter()-restart)))
