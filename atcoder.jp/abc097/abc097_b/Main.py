x = int(input())
s = {1}
for i in range(1, x):
    for j in range(2, x):
        if i**j <= x:
            s.add(i**j)
        else:
            break
print(max(s))