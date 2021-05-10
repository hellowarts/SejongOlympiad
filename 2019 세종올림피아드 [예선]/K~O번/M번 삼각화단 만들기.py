n = int(input())
count = 0
for a in range(1,n//3+1):
    for b in range(a,n-1):
        c = n - (a+b)
        if(c < a+b and a <= b and b <= c):
            count += 1
print(count)
