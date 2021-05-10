def solve(data):
    plus = 0
    for i in data:
        if(plus == 0 and ord(i) == ord(')')):
            print("NO")
            return
        if ord(i) == ord('('):
            plus += 1
        if ord(i) == ord(')'):
            plus -= 1
    if plus == 0:
        print("YES")
        return
    else:
        print("NO")
        return 
        

data = input()
solve(data)
