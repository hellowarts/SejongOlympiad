n = int(input())
St = [[0]*n for i in range(n)]
St_ch = [0]*n

def call(N):
    global St, St_ch, n
    St_ch[N] = 1
    for i in range(n):
        if St[N][i]:
            if not St_ch[i]:
                call(i)

for i in range(n):
        St[i] = list(map(int, input().split()))
        
count = 0
for i in range(n):
    if(not St_ch[i]):
        call(i)
        count += 1

print(count)
    
