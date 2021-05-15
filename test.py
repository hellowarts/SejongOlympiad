nM, nD, mM, mD = map(int, input().split())

month = [31,28,31,30,31,30,31,31,30,31,30,31]

day = 0

for i in range(nM, mM-1):
    day += month[i]

day += mD
day += month[nM-1] - nD

print("D-"+str(day))
