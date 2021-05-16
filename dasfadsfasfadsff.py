n = int(input())
arr = list(map(int, input().split()))

count = [0]*100000

new_arr = []

for i in arr:
    N = i
    N = str(N)
    for j in N:
        if j == '3':
            new_arr.append(i)
            count[i] += 1
            break
new_arr.sort()
new_list = []
for i in new_arr:
    if i not in new_list:
        new_list.append(i)

for i in range(len(new_list)):
    print(str(new_list[i])+":"+str(count[new_list[i]]))
    
