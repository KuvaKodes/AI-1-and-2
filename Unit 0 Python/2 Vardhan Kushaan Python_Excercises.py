import sys
import math

s = sys.argv[1]
if s == "A":
    print(sum(x := [int(v) for v in sys.argv[2:5]]))

if s == "B":
    print(sum(x := [int(v) for v in sys.argv[2:]]))

if s == "C":
    print(sum(x := [int(v) for v in sys.argv[2:] if int(v) % 3 == 0]))

if s == "D":
    x = sys.argv[2]
    y = [1,1]
    for z in range(2, int(x)):
        y.append(y[z-1] + y[z-2])
    print(y)

if s == "E":
    x, y = sys.argv[2:]
    n=[]
    for z in range(int(x), int(y)+1):
        n.append(z**2 - 3*z + 2)
    print(n)

if s == "F":
    x, y, z = [float(n) for n in sys.argv[2:5]]
    if x+ y >= z and y + z >= x and x + z >= y:
        p = (x + y + z)/2
        print(math.sqrt(p*(p-x)*(p-y)*(p-z)))
    else:
        print("Not a valid triangle!")

if s == "G":
    x = sys.argv[2]
    aCnt, eCnt, iCnt, oCnt, uCnt = 0, 0, 0, 0, 0
    for y in range(0, len(str(x))):
        p = str(x)[y]
        if p.upper() == "A":
            aCnt += 1
        if p.upper() == "E":
            eCnt += 1
        if p.upper() == "I":
            iCnt += 1
        if p.upper() == "O":
            oCnt += 1
        if p.upper() == "U":
            uCnt += 1
    x = ["A - " + str(aCnt), "E - " + str(eCnt), "I - " + str(iCnt), "O - " + str(oCnt), "U - " + str(uCnt)]
    print(x)

    