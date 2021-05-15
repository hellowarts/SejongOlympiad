n = int(input())
nums = list(map(int, input().split()))

count = [0]*1000000

for i in nums:
    try: count[i] += 1
    except: count[i]=1

nums.sort()

befor = -1

for i in range(n):
    if befor != nums[i]:
        print(str(nums[i])+":"+str(count[i+1]))
        befor = nums[i]
