pw = input()

count = [0,0,0,0]

for i in pw:
    if ord('A') <= ord(i) <= ord('Z'):
        count[0] += 1
    elif ord('a') <= ord(i) <= ord('z'):
        count[1] += 1
    elif 33 <= ord(i) <= 39:
        count[2] += 1
    elif ord('0') <= ord(i) <= ord('9'):
        count[3] += 1

cnt = 0
for i in range(4):
    if count[i] > 0:
       cnt += 1
if len(pw) < 8:
    print("NO")
elif cnt >= 2:
    print("YES")
else:
    print("NO")
