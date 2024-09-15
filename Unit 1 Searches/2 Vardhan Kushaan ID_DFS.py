import sys
from collections import deque 
from time import perf_counter
 
with open(sys.argv[1])as f:
    line_list = [line.strip() for line in f]

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

def kDFS(start, k):
    goal_state = find_goal(start)
    fringe = list()
    paren_dict = dict()
    fringe.append((start, 0, og_ancestors := set(start)))
    while fringe:
        temp_state, temp_depth, temp_ancestors = fringe.pop()
        if temp_state == goal_state:
            return k
        if temp_depth < k: 
            for child in get_children(temp_state):
                if child not in temp_ancestors:
                    new_ancestors = temp_ancestors.copy()
                    new_ancestors.add(child)
                    fringe.append((child, temp_depth+1, new_ancestors))

    return None

def idDFS(start):
    runningDepth = 0
    result = None
    while result is None:
        result = kDFS(start, runningDepth)
        runningDepth = runningDepth + 1
    return result

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


for i in range(len(line_list)):
    start = perf_counter()
    print("Line %s: %s, BFS - %s moves found in %s" % (i, line_list[i], BFS(line_list[i]), (perf_counter()-start)))
    restart = perf_counter()
    print("Line %s: %s, ID-DFS - %s moves found in %s" % (i, line_list[i], idDFS(line_list[i]), (perf_counter()-restart)))

