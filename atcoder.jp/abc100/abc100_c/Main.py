def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for aa in a:
        while aa%2==0 and aa > 0:
            aa /= 2
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()