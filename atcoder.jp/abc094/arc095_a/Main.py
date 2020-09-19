def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    
    for i in range(n):
        if a[i] <=  b[n // 2 - 1]:
            print(b[n // 2])
        elif a[i] >  b[n // 2 - 1]:
            print(b[n // 2 - 1])
        
        
if __name__ == '__main__':
    main()