# list.reverse() 를 사용하면 0을 없앨 수 없음 
n = int(input())

while(True):
    if n<=0 : break
    if n%10 != 0: print(n%10,end='')
    n = n // 10

    
