nums = input()

sum_ = 0
count = 1
for i in nums:
    sum_ += (ord(i) - 64) * (26**(len(nums)-count))
    count += 1
print(sum_)

