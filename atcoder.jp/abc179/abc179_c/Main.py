def main():
    n = int(input())
    ans = 0
    
    for a in range(1, n):
        for b in range(1, n):
            if 1 <= a * b <= n - 1:
                ans += 1
            else:
                break
           
    print(ans)

        
if __name__ == '__main__':
    main()