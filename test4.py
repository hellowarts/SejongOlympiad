def chS():
    global Stch, n
    for i in range(n):
        if(Stch[i] == 0):
            return 0
    return 1

def call2(i):
    global St, Stch, n
    Stch[i] = 1
    for j in range(n):
        if(St[i][j] == 1 and Stch[j] != 1):
            call2(j)

def call():
    global St, Stch, n
    Max = 0
    check = 0
    while True:
        if(chS()): break
        I = -1
        for i in range(n):
            if(Stch[i] != 1):
                count = 0
                Max = 0
                for j in range(n):
                    if(St[i][j] == 1 and i != j):
                        count += 1
                if(count > Max):
                    Max = count
                    I = i
        if(I != -1):
            call2(I)
        check += 1
    return check


n = int(input())

St = [[0]*n for i in range(n)]
Stch = [0]*n

for i in range(n):
    St[i] = list(map(int,input().split()))

check = call()
print(check)

