def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    
    for i in range(1, len(a)):
        humidai = max(0, a[i-1] - a[i])
        ans +=  humidai
        a[i] += humidai
    print(ans)
        
        
if __name__ == '__main__':
    main()