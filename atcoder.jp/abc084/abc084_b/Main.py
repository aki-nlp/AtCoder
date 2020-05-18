a, b = map(int, input().split())
s = input()
if (s.count('-') == 1 
    and len(s.split('-')[0]) == a and  len(s.split('-')[1]) == b) :
    print('Yes')
else:
    print('No')