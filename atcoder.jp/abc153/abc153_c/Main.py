n, k = map(int, input().split())
h =  list(map(int, input().split()))

def solve():
    global n, k, h
    if n <= k:
        return 0
    s = sum(h)
    h = sorted(h, reverse=True)
    for i in range(k):
        s -= h[i]
    return s

print(solve())