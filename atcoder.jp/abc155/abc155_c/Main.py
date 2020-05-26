import collections

n = int(input())
d = {}
for _ in range(n):
    s = input()
    if d.get(s):
        d[s] += 1
    else:
        d[s] = 1
m = 0
ans = []
for k, v in d.items():
    if m < v:
        m = v
        ans = [k]
    elif m == v:
        ans.append(k)
for i in sorted(ans):
    print(i)