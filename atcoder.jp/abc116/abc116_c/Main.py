def main():
    n = int(input())
    h = list(map(int, input().split()))
    x = [0] * n
    ans = 0
    
    for _ in range(110):
        pre  = False
        for i in range(n):
            if x[i] < h[i]:
                x[i] += 1
                if pre == False:
                    ans += 1
                    pre = True
            else:
                pre = False 
            
    print(ans)
    
    
if __name__ == '__main__':
    main()