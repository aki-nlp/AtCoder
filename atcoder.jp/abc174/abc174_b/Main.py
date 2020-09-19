def main():
    n, D = map(int, input().split())
    ans = 0
    
    for _ in range(n):
        x, y = map(int, input().split())
        d = (x**2 + y**2)**(0.5)
        if d <= D:
            ans += 1
        
    print(ans)
   
    
if __name__ == '__main__':
    main()