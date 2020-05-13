n = int(input())
l = [(i+1)*(j+1) for i in range(9) for j in range(9)]
if n in l:
    print('Yes')
else:
    print('No')