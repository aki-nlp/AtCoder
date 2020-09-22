def powmod(a, n):
    MOD = 10**9 + 7
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % MOD
        a = a * a % MOD;
        n >>= 1
    return res
            
def main():
    MOD = 10**9 + 7
    n = int(input())
    ans = powmod(10, n) - 2 * powmod(9, n) + powmod(8, n)
    ans %= MOD
    ans = (ans+MOD)%MOD
    print(ans)
        
if __name__ == '__main__':
    main()
