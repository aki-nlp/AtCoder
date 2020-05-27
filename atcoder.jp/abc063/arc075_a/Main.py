def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]
      
    ans = sum(s)
    if ans % 10 != 0:
        print(ans)
    else:
        a = 10**9
        for ss in s:
            if ss % 10 != 0:
                a = min(a, ss)
        if a!=10**9:
            print(ans - a)
        else:
            print(0)
    
if __name__ == '__main__':
    main()