n, m, q = input().split()
n = int(n)
m = int(m)
q = int(q)

map_ = [[0]*m for i in range(n)]

for i in range(q):
    a,b,c,d,k = input().split()
    a= int(a)
    b= int(b)
    c= int(c)
    d= int(d)
    k= int(k)
    for j in range(a-1, c):
        for K in range(b-1, d):
            map_[j][K] += k

for i in range(n):
    for j in range(m):
        print(map_[i][j], end=" ")
    print()

