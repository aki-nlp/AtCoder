n = int(input())

h = n // 3600
m = (n - h * 3600)//60
s = n - h * 3600 - m * 60

print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), sep=':')