def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = [0]
    y = []
    z = []
    
    su = 0
    for i in a:
        su += i
        x.append(su)
        
    su = 0
    for i in x:
        su += i
        y.append(su)
    
    before = y[0]
    for i in x:
        before = max(before, i)
        z.append(before)

    ans = 0
    for i in range(n):
        ans = max(ans, y[i] + z[i+1])
    print(ans)
    
    
        
if __name__ == '__main__':
    main()
