def f(n):
    r = 1
    sum_ = 0
    for i in range(1,(n+1)//2+1):
        sum_ += 2*i
    sum_ *= 2
    if(n%2==0): r = r + sum_ - 2
    else : r = r + sum_ - ((n+1)//2)*2 -2
    
    return r

n = int(input())
print(f(n))

