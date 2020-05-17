import math
 
a, b, h, m = map(int, input().split())
a_h = h*30 + m*0.5
a_m = m* 6
angle = abs(a_h-a_m)
 
print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(angle))))
