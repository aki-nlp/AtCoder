def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::2]
    ans = 0
    for aa in a:
        if aa%2 == 1:
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()