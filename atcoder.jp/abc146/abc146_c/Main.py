def main():
    a, b, x = map(int, input().split())
    
    def f(n):
        return a * n + b * len(str(n))

    def seach():
        l = 0
        r = 10**10
        while True:
            i = (l + r) // 2
            if r - l <= 1:
                if f(r) == x:
                    return r
                else:
                    return l
            if f(i) < x:
                l = i
            elif f(i) > x:
                r = i
            else: 
                return i
    
    ans = seach()
    if ans > 10**9:
        print(10**9)
    else:
        print(ans)
        
    
if __name__ == '__main__':
    main()