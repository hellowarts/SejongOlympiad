n = int(input())

a = [[0]*n for i in range(n)]
i=0
j=n//2

for k in range(1,n**2+1):
    a[i][j] = k

    if k % n == 0 :
        i+=1
    else:
        i-=1
        if i<0:
            i = n-1
        j+=1
        if j == n:
            j=0

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end=" ")
    print()
