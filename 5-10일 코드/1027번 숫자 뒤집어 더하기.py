def check(num): # 회문자인지 체크
    ch = True
    
    for i in range(len(num) // 2):
        if num[i] != num[-1 -i]:
            ch = False
            break
    return ch

def reverse_plus(num): # 뒤집은 후 더하기
    rNum = ""
    for i in num:
        rNum = i + rNum
    return str(int(num) + int(rNum))
    
num = input()
count = 0
while(check(num) != True):
    num = reverse_plus(num)
    count +=1
    
print(count,num)
