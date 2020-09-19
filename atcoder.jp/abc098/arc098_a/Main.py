def main():
    n = int(input())
    s = input()
    
    a = [0] * (n)
    b = [0] * (n)
    for i in range(1, n):
        if s[i - 1] == 'W':
            a[i] = a[i - 1] + 1
        else:
            a[i] = a[i - 1]
        if s[n- i] == 'E':
            b[n - i - 1] = b[n - i ] + 1
        else:
            b[n- i - 1] = b[n - i ]
    ans = 10**9
    for aa, bb in zip(a, b):
        ans = min(ans, aa++bb)
    print(ans) 
        
if __name__ == '__main__':
    main()