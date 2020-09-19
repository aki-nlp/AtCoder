def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    tmp = 1
    for i in range(n):
        if a[i] == tmp:
            tmp +=1
        else:
            ans += 1
    if ans == n and n != 1:
        print(-1)
    else:
        print(ans)
    
      
if __name__ == '__main__':
    main()