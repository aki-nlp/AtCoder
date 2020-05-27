def main():
    n = int(input())
    h = list(map(int, input().split()))
    
    pre = h[0]
    now = -1
    ans = 0
    for hh in h:
        if hh <= pre:
            now += 1
            ans = max(ans, now)
        else:
            now = 0
        pre = hh
    print(ans)
    
if __name__ == '__main__':
    main()