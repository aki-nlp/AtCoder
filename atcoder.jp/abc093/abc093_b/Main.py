a, b, k = map(int, input().split())
s = set()
for i in range(a, a+k):
    if a <=  i <= b:
        s.add(i)
for i in range(b-k+1, b+1):
    if a <=  i <= b:
        s.add(i)
for i in sorted(s):
    print(i)