s = input()
t = input()
u = list('atcoder')

for x, y in zip(s, t):
    if x =='@' and y in u:
        continue
    elif y =='@' and x in u:
        continue
    elif x != y:
        print('You will lose')
        break
else:
    print('You can win')