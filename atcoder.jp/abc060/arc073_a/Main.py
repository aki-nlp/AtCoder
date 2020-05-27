def main():
    n, T = map(int, input().split())
    t = list(map(int, input().split()))
    
    ans = T
    pre = t[0]
    for tt in t:
        if tt - pre < T:
            ans += tt - pre
        else:
            ans += T
        pre = tt
    print(ans)
               
if __name__ == '__main__':
    main()