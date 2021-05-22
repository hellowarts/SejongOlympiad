n, m = map(int, input().split()) # 정수 입력

maps = [[0]*m for i in range(n)] # 맵 제작

for i in range(n): # 제작한 맵에 데이터 입력
    maps[i] = list(map(str, input().split()))

print(maps)
