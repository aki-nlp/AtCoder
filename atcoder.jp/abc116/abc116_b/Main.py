s = int(input())

def fn(n):

    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
        
for i in range(1, 10**8):
    if i == 1:
        a = s
    else:
        a = fn(a)
    if a ==1 or a == 2 or a == 4:
        print(i+3)
        break