n = int(input())
for i in range(0, 7):
    if n >= 2**(6-i):
        print(2**(6-i))
        break