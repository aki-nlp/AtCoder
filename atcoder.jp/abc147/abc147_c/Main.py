def main():
    xy = []
    n = int(input())
    for _ in range(n):
        a = int(input())
        xy.append([list(map(int, input().split())) for _ in range(a)])
    ans = 0
    
    for a in range(2**n):
        c = []
        for b in range(n):
            c.append(a >> b & 1)
       
        flag = True
        for i in range(n):
            if c[i] == 1:
                for x, y in xy[i]:
                    if c[x - 1] != y:
                        flag = False
                        
        if flag:
            ans = max(ans, sum(c))
    
    print(ans)
        
    
if __name__ == '__main__':
    main()