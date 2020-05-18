n = int(input())

l = [0] * 100
l[0] = 2
l[1] = 1

if n == 0 or n == 1:
    print(l[n])
if n>=2:
    for i in range(2, n+1):
        l[i] = l[i-1] + l[i-2]
    print(l[n])
    
