n = int(input())
s = []
p = []

for _ in range(n):
    a, b = input().split()
    s.append(a)
    p.append(int(b))
    
m = sum(p)/2
    
for a, b  in zip(s, p):
    if b > m:
        print(a)
        break
else:
    print('atcoder')
    
    
