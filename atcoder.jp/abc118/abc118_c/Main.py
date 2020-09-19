from fractions import gcd


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for aa in a:
        ans = gcd(ans, aa)
        
    print(ans)
    
    
if __name__ == '__main__':
    main()