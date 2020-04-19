n,m=map(int, input().split())
a=list(map(int, input().split()))
s=sum(a)
day=n-s
print(day if day>=0 else -1)