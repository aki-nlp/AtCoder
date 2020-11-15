def main():
    n, w = map(int, input().split())
    SIZE = 2 *(10**5) + 10
    use =  [0] * SIZE
    for _ in range(n):
        s, t, p = map(int, input().split())
        use[s]  += p
        use[t] -= p
    su = 0;
    for i in range(SIZE):
        if su > w:
            print('No')
            return
        su += use[i];
    print('Yes')
        
    
if __name__ == '__main__':
    main()
