w = input()

for i in set(w):
    if w.count(i) % 2 == 1:
        print('No')
        break
else:
    print('Yes')