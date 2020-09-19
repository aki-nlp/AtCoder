def main():
    MOD = 10**9 + 7
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
   
    a_sum = sum(a)
    
    for i in range(n-1):
        a_sum -= a[i]
        ans += a[i] * a_sum
        ans %= MOD
    print(ans)
        
        
if __name__ == '__main__':
    main()