s = input()
a = int(input())

name = []
for i in s:
    for j in s:
        name.append(i+j)
print(name[a-1])