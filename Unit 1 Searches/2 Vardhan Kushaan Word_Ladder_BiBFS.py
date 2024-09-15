import sys 
from collections import deque
from time import perf_counter

with open("words_06_letters.txt")as f:
    line_list = [line.strip() for line in f]

with open("puzzles_normal.txt") as f1:
    line_list2 = [line.strip().split() for line in f1]

def one_char_away(word1, word2):
    count = 0
    for ind in range(len(word1)):
        if word1[ind] != word2[ind]:
            count = count + 1
    if count == 1:
        return True
    return False

start = perf_counter()
children_dict = dict()
for word in line_list:
    children_dict[word] = list()
    for word2 in line_list:
         if one_char_away(word, word2):
            children_dict[word].append(word2)
end = perf_counter()
print("Time to create the data structure was: %s" % (end-start))
print("There are %s items in this dict" % len(children_dict))


def get_children(start): 
    return children_dict[start]


def BFS(start, goal):
    fringe = deque()
    visited = set()
    paren_dict = dict()
    fringe.append(start)
    visited.add(start)
    paren_dict[start] = None
    while fringe:
        temp = fringe.popleft()
        if temp == goal:
            lst_of_moves = list()
            g = temp
            lst_of_moves.append(g)
            while paren_dict[g] is not None:
                g = paren_dict[g]
                lst_of_moves.append(g)
            return (len(lst_of_moves), lst_of_moves)
        for child in get_children(temp):
            if child not in visited:
                fringe.append(child)
                visited.add(child)
                paren_dict[child] = temp
    return (None, list())

def BiBFS(start, goal):
    start_goal_state = goal
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
            return ((len(lst_of_moves_backwards) + len(lst_of_moves_forwards)), newList := (list((reversed(lst_of_moves_forwards))) + lst_of_moves_backwards))
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
            return ((len(lst_of_moves_back) + len(lst_of_moves_forw)), newList := (list((reversed(lst_of_moves_forw))) + lst_of_moves_back))
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
    return (None, list())

start2 = perf_counter()
for i in range(len((line_list2))):
    print("Line: %s" % i)
    length, path = BFS(line_list2[i][0],line_list2[i][1])
    if length is None:
        print("No Solution!")
    else:
        print("Bfs Length is: %s" % length)
    print("\n".join(reversed(path)))
    print("")
end2 = perf_counter()

print("Time to solve all of these puzzles was: %s seconds" % (end2-start2))
start3 = perf_counter()
for i in range(len((line_list2))):
    print("Line: %s" % i)
    length, path = BiBFS(line_list2[i][0],line_list2[i][1])
    if length is None:
        print("No Solution!")
    else:
        print("Bfs Length is: %s" % length)
    print("\n".join((path)))
    print("")
end3 = perf_counter()

print("Time to solve all of these puzzles was: %s seconds" % (end3-start3))
