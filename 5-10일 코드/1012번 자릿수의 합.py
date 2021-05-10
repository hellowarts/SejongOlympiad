n = input()
sum_ = 0
while(10 <= int(n)):
    for i in range(len(n)):
        sum_ += int(n[i])
    n = str(sum_)
    sum_ = 0
print(int(n))


    
