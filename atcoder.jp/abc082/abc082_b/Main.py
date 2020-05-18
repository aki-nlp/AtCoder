s = input()
t = input()
s = ''.join(sorted(list(s)))
t = ''.join(sorted(list(t), reverse=True))
if s < t:
    print('Yes')
else:
    print('No')