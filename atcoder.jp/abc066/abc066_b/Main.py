s = input()
for i in range(1, len(s)):
    l = len(s[0:-i])
    if l % 2 == 0 and s[0:l//2] == s[l//2:-i]:
        print(l)
        break
