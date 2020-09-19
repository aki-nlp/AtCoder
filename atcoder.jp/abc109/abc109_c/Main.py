from fractions import gcd


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] =abs(a[i] - x)
 
    ans = 0
    for aa in a:
        ans = gcd(aa, ans)
    print(ans)

    
if __name__ == '__main__':
    main()