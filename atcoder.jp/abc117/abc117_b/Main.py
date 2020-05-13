n = int(input())
l = list(map(int, input().split()))
m = max(l)
if  m < sum(l) - m:
    print('Yes')
else:
    print('No')