def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

n = int(input())
l = sorted(divisor(n))

if len(l) % 2 == 1:
    i = l[len(l)//2]
    ans = i * 2 - 2
else:
    i = l[len(l)//2 - 1]
    j = l[len(l)//2]
    ans = i  + j - 2
    
print(ans)