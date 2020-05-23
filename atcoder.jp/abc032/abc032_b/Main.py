s = input()
k = int(input())

c = set()
i = 0
while i + k <= len(s):
    c.add(s[i:i+k])
    i += 1

print(len(c))