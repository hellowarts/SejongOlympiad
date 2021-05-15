nums = list(map(int, input().split()))
nums.sort()

if(nums[0] + nums[1] > nums[2]):
    print("Yes")
else:
    print("No")
