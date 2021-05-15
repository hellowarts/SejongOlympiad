num , switch = input().split()
switch = int(switch)

length = len(num)
num_f = [0]* length
num_s = [0]* length

for i in range(length):
    num_f[i] = int(num[i])

for i in range(length):
    ch = i + switch
    ch %= length
    num_s[ch] = num_f[i]
for i in num_s:
    print(i, end="")
