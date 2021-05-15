n = int(input())
nums = list(map(int, input().split()))

count = [0]*1000000

for i in nums:
    try: count[i] += 1
    except: count[i]=1

nums.sort()

befor = -1

print("3:"+str(count[3]))
print("13:"+str(count[13]))
print("31:"+str(count[31]))
print("303:"+str(count[303]))
