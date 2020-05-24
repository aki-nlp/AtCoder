m = int(input())
m = m/1000

if m < 0.1:
    print('0'.zfill(2))
elif 0.1 <= m <= 5:
    print(str(int(m*10)).zfill(2))
elif 6 <= m <= 30:
    print(int(m)+50)
elif 35 <= m <=70:
    print(int((m-30)/5+80))
elif m > 70:
    print(89)