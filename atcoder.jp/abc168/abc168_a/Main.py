n = int(input())
a = [2, 4, 5, 7, 9]
b = [0, 1 ,6, 8]
c = [3]

n = n % 10
if n in a:
    print('hon')
if n in b:
    print('pon')
if n in c:
    print('bon')