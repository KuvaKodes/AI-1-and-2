from heapq import heappush, heappop, heapify
import sys 
from time import perf_counter
start = perf_counter()

f1, f2, f3 = sys.argv[1:4]
with open(f1) as f:
    line_list1 = [int(line.strip()) for line in f]

with open(f2) as f:
    line_list2 = [int(line.strip()) for line in f]

with open(f3) as f:
    line_list3 = [int(line.strip()) for line in f]

set1 = set(line_list1)
set2 = set(line_list2)
set3 = set(line_list3)
uniquelist1 = list(set1)
heapify(uniquelist1)
file2dict = dict()
#convert to dictionary with the counts and any value is 2 or greater than work w it. 
print("#1: %s" % len(set1.intersection(set2)))

x_dict = dict.fromkeys(line_list1)
count = 0
t = []
for key in x_dict: 
    count += 1
    if count % 100 == 0:
        t.append(key)
print("#2: %s"  % sum(t))

prob3count = 0
for x2 in line_list1:
    if x2 in set3:
        prob3count += 1 

for x3 in line_list2: 
    if x3 in set3:
        prob3count += 1

print("#3: %s" % prob3count)

list1 = []
for x in range(0,10):
    list1.append(heappop(uniquelist1))

print("#4: %s" % list1)

for x in line_list2:
    file2dict[x] = file2dict.get(x, 0) + 1

templist = []
for x in file2dict: 
    if file2dict[x] >= 2:
        templist.append(x * -1)
heapify(templist)

finlist = []
for x in range(0,10):
    finlist.append(heappop(templist) * -1)
print("#5: %s" % finlist)

heaplist = []
trackerset = set()
finset = set()
for x in line_list1: 
    if x not in trackerset:
        trackerset.add(x)
        heappush(heaplist, x)
    if x % 53 == 0:
        finset.add(heappop(heaplist))

print("#6: %s" % sum(finset))
    

end = perf_counter()
print("Total time: ", end - start)