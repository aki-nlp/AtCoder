o = input()
e = input()

for x, y in zip(o, e):
    print(x + y, end = '')
if len(o) != len(e):
    print(o[-1])
else:
    print()