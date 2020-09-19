def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    
    ans = 0
    for i in range(1, n +1):
        ans = max(ans, sum(a[0][:i])+sum(a[1][i - 1:]))
    
    print(ans)
    
    
if __name__ == '__main__':
    main()