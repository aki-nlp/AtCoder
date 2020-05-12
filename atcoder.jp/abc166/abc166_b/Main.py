n, k = map(int, input().split())
a=set()
for _ in range(k):
    d = (int(input()))
    a = a | (set(map(int, list(input().split()))))
print(n - len(a))