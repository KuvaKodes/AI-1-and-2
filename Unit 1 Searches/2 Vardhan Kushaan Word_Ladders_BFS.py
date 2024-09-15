import sys 
from collections import deque
from time import perf_counter

with open(sys.argv[1])as f:
    line_list = [line.strip() for line in f]

with open(sys.argv[2]) as f1:
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


start2 = perf_counter()
for i in range(len((line_list2))):
    print("Line: %s" % i)
    length, path = BFS(line_list2[i][0],line_list2[i][1])
    if length is None:
        print("No Solution!")
    else:
        print("Length is: %s" % length)
    print("\n".join(reversed(path)))
    print("")

end2 = perf_counter()

print("Time to solve all of these puzzles was: %s seconds" % (end2-start2))
