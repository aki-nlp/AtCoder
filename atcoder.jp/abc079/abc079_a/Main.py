n = list(map(int, input()))

if (n[0]==n[1] and n[1]==n[2]) or (n[1]==n[2] and n[2]==n[3]):
    print('Yes')
else:
    print('No')