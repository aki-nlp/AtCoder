def main():
    n, m = map(int, input().split())
    ks = [list(map(int, input().split())) for _ in range(m)]
    p = list(map(int, input().split()))
    ans = 0
    

    for i in range(2**n):
        a = []
        flag = True
        for j in range(n):
            a .append(i>>j & 1)
        ok = 0
        for j in range(m):
            switch = 0
            for s in ks[j][1:]:
                switch += a[s - 1]
            if switch % 2 != p[j]:
                flag = False
        if flag:
            ans +=1
            
    print(ans)
                
    
if __name__ == '__main__':
    main()