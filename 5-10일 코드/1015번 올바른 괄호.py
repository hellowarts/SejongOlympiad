def solve(data):
    plus = 0
    for i in data:
        if(plus == 0 and i == ')'):
            print("bad")
            return
        if i == '(':
            plus += 1
        if i == ')':
            plus -= 1
    if plus == 0:
        print("good")
        return
    else:
        print("bad")
        return 
        

data = input()
solve(data)
