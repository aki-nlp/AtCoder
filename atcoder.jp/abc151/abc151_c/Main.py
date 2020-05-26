n, m = map(int, input().split())

ac = [0]*(n+1)
wa = [0]*(n+1)

for _ in range(m):
    a, b = input().split()
    a = int(a)
    if b == 'AC':
        ac[a] = 1
    else: 
        if ac[a] == 0:
            wa[a] = wa[a] + 1

for i in range(n+1):
    wa[i] = wa[i] * ac[i]

print(sum(ac), sum(wa))

