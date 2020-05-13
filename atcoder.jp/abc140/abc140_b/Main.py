n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

before = a[0]
c_sum = 0
for i in range(1, n):
    if a[i] == before+1:
        c_sum += c[before-1]
    before = a[i]
print(sum(b) + c_sum)