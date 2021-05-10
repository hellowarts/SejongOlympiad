def prime_scan(n):
    if n == 1:
        return 0
    for i in range(2,n//2):
        if n%i == 0:
            return 0
    return 1

count = 0
N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    if prime_scan(arr[i]):
        count += 1
print(count)
