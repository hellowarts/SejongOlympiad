def merge(m, middle, n):
    global arr, sort, count
    i = m
    j = middle + 1
    k = m
    while i <= middle and j <= n:
        if arr[i] <= arr[j]:
            sort[k] = arr[i]
            i += 1
        else:
            count += j-k
            sort[k] = arr[j]
            j += 1
        k += 1
    if i > middle:
        for t in  range(j, n + 1):
            sort[k] = arr[t]
            k += 1
    else:
        for t in range(i, middle + 1):
            sort[k] = arr[t]
            k += 1
    for t in range(m, n + 1):
        arr[t] = sort[t] 
def mergeSort(m,n):
    global arr
    if(m < n):
        middle = (m+n) // 2
        mergeSort(m, middle)
        mergeSort(middle + 1, n)
        merge(m , middle, n)

N = int(input())
arr = list(map(int, input().split()))

count = 0
sort = [0]*N

mergeSort(0, N-1)

print(count)
