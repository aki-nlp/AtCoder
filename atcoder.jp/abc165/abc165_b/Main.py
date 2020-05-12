x = int(input())
money = 100
ans = 0

while True:
    money += int(money*0.01)
    ans += 1
    if  money >= x:
        break
print(ans)