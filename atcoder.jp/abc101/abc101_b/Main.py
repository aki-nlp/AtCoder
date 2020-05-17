n = int(input())
t  = sum(list(map(int, str(n))))
print('Yes' if n%t==0 else 'No')