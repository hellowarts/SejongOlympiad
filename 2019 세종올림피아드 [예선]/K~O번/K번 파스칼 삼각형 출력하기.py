def f(a, b):
    if(a == 0 or b == 0 or a==b): return 1
    return f(a-1, b) + f(a-1,b-1)

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(f(i,j), end=" ")
    print()
