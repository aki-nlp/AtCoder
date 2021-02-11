def main():
    n =  int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(n):
        for j in range(i+1, n):
            a = (p[i][1] - p[j][1]) / (p[i][0] - p[j][0])
            if abs(a) <= 1:
                ans += 1     
    print(ans)

                
if __name__ == '__main__':
    main()