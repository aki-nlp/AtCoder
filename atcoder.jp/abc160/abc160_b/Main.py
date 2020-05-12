x = int(input())
happy_500 = x //500
happy_50 = (x - happy_500*500) // 5
happy_500 *= 1000
happy_50 *= 5
print(happy_500+happy_50)