import collections

n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s)
print(c.most_common()[0][0])