s = input()

c1= c2 = 0
for i in s[2:]:
    if i == 'C':
        c1 += 1
    else:
        if i!=i.lower():
            c2 +=1
if s[0] == 'A' and s[1] == s[1].lower() and c1==1 and c2==0 and s[-1] != 'C':
    print('AC')
else:
    print('WA')