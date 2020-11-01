def main():
    n = int(input())
    ans = 0
    
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        ans += (b*(b+1)//2) -(a*(a+1)//2)
        
    print(ans)
    
        
if __name__ == '__main__':
    main()
