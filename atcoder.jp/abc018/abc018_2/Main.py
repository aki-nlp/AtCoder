s = input()
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

for l, r in lr:
    t = s[l-1:r][::-1]
    s=s[:l-1]+t+s[r:]
print(s)