n = int(input())
pw = input()
for i in pw:
    scan = ord(i)
    if ord("A") <= scan <= ord("Z"):
        scan += n
        if scan > ord("Z"):
            scan -= ord("A")
            scan %= 26
            scan += ord("A")
        print(chr(scan), end="")
    else:
        scan -= ord("0")
        scan += n
        if scan > 9:
            scan %= 10
        print(scan, end="")

    
