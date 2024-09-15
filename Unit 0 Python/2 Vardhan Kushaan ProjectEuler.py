from functools import total_ordering
import sys
from heapq import heapify, heappop, heappush
from time import perf_counter
start = perf_counter()

def is_prime(x):
    n = x ** 0.5
    if x % 2 == 0 and x != 2:
        return False
    for g in range(3, int(n)+1, 2):
        if x % g == 0:
            return False
    return True    

print("#1: %s" % sum((x:= [y for y in range(0,1000) if y % 3 == 0 or y % 5 == 0]))) #Problem 1 

#problem 3
fibseq = [1,2]
id = 2
while fibseq[-1] <= 4000000:
    fibseq.append(fibseq[id-2]+fibseq[id-1])
    id += 1

print("#2: %s" % sum((x:= [y for y in fibseq if y % 2 == 0])))

#problem 3

def prime_factorize(x):
    lst_of_factors = list()
    for y in range(2, int(x**0.5)+1):
        if is_prime(y) and x % y == 0:
            lst_of_factors.append(y)
            x = x/y
    return lst_of_factors

print("#3: %s" % prime_factorize(600851475143)[-1])


#problem 4
def is_palindrome(x):
    pali_str = str(x)
    if pali_str == pali_str[::-1]:
        return True
    else:
        return False

curr_largest = 0
for x in range(100,1000):
    for y in range(100, 1000):
        max_val = x*y
        if is_palindrome(max_val) and max_val > curr_largest:
            curr_largest = max_val

print("#4: %s" % curr_largest)

#problem 5 
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    lcm = (x * y)//gcd(x,y)
    return lcm

smallest_max = 1
for x in range(2, 20):
    smallest_max = lcm(smallest_max, x)

print("#5 %s" % smallest_max)



#problem 6
print("#6: %s" % ((sum(list(range(1,101)))**2) - sum((x:= [y**2 for y in range(1,101)]))))

#problem 7
x = 0
lst  = list()
while len(lst) <= 10001:
    if is_prime(x):
        lst.append(x)
    x = x+1
print("#7: %s" % lst[-1])


#problem 8

num_string = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385" +\
"861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689" +\
"664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589" +\
"072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333" +\
"001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797" +\
"784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844" +\
"031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124" +\
"566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245" +\
"544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050" +\
"7754100225698315520005593572972571636269561882670428252483600823257530420752963450"

proddy = 0
for x in range(0,987):
    templist = [int(y) for y in num_string[x:x+13]]
    tempproduct = 1
    for n in templist:
        tempproduct = tempproduct * n
    if tempproduct > proddy:
        proddy = tempproduct

print("#8: %s" % proddy) 

#problem 9
def isPythagorean(x, y, z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False

toRet = 0
for x in range(1,1000):
    for y in range(1,1000):
        z = 1000 - x - y
        if isPythagorean(x,y,z):
            toRet = x*y*z

print("#9: %s" % toRet)

#problem 11

data = [[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],

       [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],

       [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],

       [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],

       [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],

       [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],

       [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],

       [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],

       [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],

       [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],

       [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],

       [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],

       [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],

       [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],

       [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],

       [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],

       [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],

       [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],

       [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],

       [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]]

running_max = 0
for r in data: 
    for g in range(0, len(r)-3):
        if (r[g]*r[g+1]*r[g+2] * r[g+3]) > running_max:
            running_max = r[g]*r[g+1]*r[g+2] * r[g+3]

for col_index, col in enumerate(data[0]):
    for row_index in range(0, len(data)-3):
        if data[row_index][col_index] * data[row_index+1][col_index] * data[row_index+2][col_index] * data[row_index+3][col_index] > running_max:
            running_max = data[row_index][col_index] * data[row_index+1][col_index] * data[row_index+2][col_index] * data[row_index+3][col_index]

for row_in in range(0, len(data)-3):
    for col_in in range(0, len(data[0])-3):
        if data[row_in][col_in] * data[row_in+1][col_in+1] * data[row_in+2][col_in+2] * data[row_in+3][col_in+3] > running_max:
            running_max = data[row_in][col_in] * data[row_in+1][col_in+1] * data[row_in+2][col_in+2] * data[row_in+3][col_in+3]

for row_ind in range(0, len(data)-3):
    for col_ind in range(len(data[0])-1, 2, -1):
        if data[row_ind][col_ind] * data[row_ind+1][col_ind-1] * data[row_ind+2][col_ind-2] * data[row_ind+3][col_ind-3] > running_max:
            running_max = data[row_ind][col_ind] * data[row_ind+1][col_ind-1] * data[row_ind+2][col_ind-2] * data[row_ind+3][col_ind-3]

print("#11: %s" % running_max)

#problem 12
def factor_list(x):
    lst_of_facs = list()
    for n in range(1, int(x**0.5)):
        if x % n == 0:
            lst_of_facs.append(n)
            lst_of_facs.append(x/n)
    return lst_of_facs

g = 1
count = 1
while len(factor_list(g)) <= 500:
    count = count + 1
    g = (count * (count+1))//2

print("#12: %s" % g)

#problem 14

def generate_collatz(start): 
    collatz_seq = [start]
    while collatz_seq[-1] != 1:
        if collatz_seq[-1] % 2 == 0:
            collatz_seq.append(collatz_seq[-1]//2)
        else:
            collatz_seq.append((3*collatz_seq[-1])+1)
    return collatz_seq

largest_collatz = 0
toRet = 0
for n in range(1,1000000):
    temp_collatz = len(generate_collatz(n)) 
    if temp_collatz > largest_collatz:
        largest_collatz = temp_collatz
        toRet = n

print("#14: %s" % toRet)

#problem 28

spiral = list(range(1, 1001*1001+1))

diag_sum = 1
factor = 0
cnt = 0
while cnt + ((factor+2)*4) < (1001*1001):
    factor = factor + 2
    for g in range(0,4):
        cnt = cnt+factor
        diag_sum = diag_sum + spiral[cnt]

print("#28: %s" % diag_sum)

#problem 29

print("#29: %s" % len(h := {a**b for a in range(2,101) for b in range(2,101)}))



end = perf_counter()
print("Total time: ", end - start)