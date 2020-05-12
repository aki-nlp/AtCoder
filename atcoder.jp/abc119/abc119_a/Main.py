s = input()
s = s.split('/')
s = list(map(int, s))
if s[0]<2018 or (s[0]==2019 and s[1]<=4 and s[2]<=30):
    print('Heisei')
else:
    print('TBD')