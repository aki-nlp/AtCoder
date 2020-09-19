def main():
    n, k = map(int, input().split())
    
    ans = 0
    for j in range(1, n+1):
        i = 0
        while True:
            if j*(2 ** i) >= k:
                ans += 1/  (n * (2 ** i))
                break
            else:
                i += 1
            
    print(ans)

    
if __name__ == '__main__':
    main()