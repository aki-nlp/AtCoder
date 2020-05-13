s = input()
acgt = ['A', 'C', 'G', 'T']
tmp = 0
ans = 0
for i in s:
    if i in acgt:
            tmp +=1
            ans = max(ans, tmp)
    else:
        ans = max(ans, tmp)
        tmp = 0

print(ans)