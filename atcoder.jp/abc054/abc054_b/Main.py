n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]

def check():
    for i in range(n):
            for j in range(n):
                if i + m <= n and j + m <= n:
                    aa = []
                    for k in range(m):
                        aa.append(a[i + k][j : j+m])
                    if aa == b:
                        return 'Yes'
    return 'No'

print(check())