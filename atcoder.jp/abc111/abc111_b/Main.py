n = int(input())
m = list(str(n))
if m[0] == m[1] == m[2]:
    print(n)
else:
    for i in range(1, 10):
        if n<=i*111:
            print(i*111)
            break