n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
count_d = int(input())

count = 0
time = 0

for i in range(1,101):
    if(count>= count_d):
        time = i - 1
        break;
    for j in arr:
        if(i%j == 0):
            count += 1
print(time)

