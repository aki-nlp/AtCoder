def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 0
    i = m
    for a, b in  sorted(ab):
        if i >= 0:
            ans += a * min(i, b)
            i -= min(i, b)
    
    print(ans)
            

if __name__ == '__main__':
    main()