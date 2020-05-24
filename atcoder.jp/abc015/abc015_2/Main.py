import math
n = int(input())
a = list(map(int, input().split()))

if n == a.count(0):
    print(0)
else:
    print(math.ceil(sum(a)/(n-a.count(0))))