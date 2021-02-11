def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        m = min(a)
        print(a.index(m) + 1)
        return
    tournament1 = max(a[:2**(n-1)])
    tournament2 = max(a[2**(n-1):])
    m = min(tournament1, tournament2)
    print(a.index(m) + 1)
    
                
if __name__ == '__main__':
    main()
