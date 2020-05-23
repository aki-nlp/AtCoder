ans = [0]*6
s = input()
for i in s:
    ans[ord(i)-ord('A')] += 1
print(' '.join(map(str, ans)))