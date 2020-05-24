s = input()
x = ['a', 'i', 'u', 'e', 'o']
for i in s:
    if i not in x:
        print(i, end='')
print()