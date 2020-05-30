def main():
    a, b, c, x, y = map(int, input().split())
    
    t1 = a * x + b * y
    t2 = c * max(x, y) * 2
    if x >= y:
        t3 = c * y * 2 + a * (x - y)
    else:
        t3 = c * x * 2 + b * (y - x)
        
    print(min(t1, t2, t3))
    
    
if __name__ == '__main__':
    main()