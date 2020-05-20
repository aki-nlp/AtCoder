n = int(input())
s = [list(input()) for _ in range(n)]

for j in range(n):
    for i in range(n):
        print(s[n-i-1][j], end='')
    print()