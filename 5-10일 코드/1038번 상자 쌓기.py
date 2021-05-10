n = 0
arr = []
for i in range(31):
    arr.append(0)

def p(index):
    global arr
    for i in range(index):
        print(arr[i], end=" ")
    print()

def solve(k ,N, index):
    global arr,n
    for i in range (k, 0, -1):
        if index == 0:
            arr[index] = i
            solve(k-i, i, index+1)
        else:
            arr[index] = i
            if i<=arr[index-1]:
                solve(k-i, N+i, index+1)
    if(n==N):
        p(index)
        
n = int(input())
solve(n,0,0)
                

