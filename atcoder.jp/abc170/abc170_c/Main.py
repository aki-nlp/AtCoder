def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))

    for i in range(51):
        a = x - i
        b = x + i
        if a not in p and a >= 0:
            print(a)
            return
        if b not in p and b <= 101:
            print(b)
            return
    
        
if __name__ == '__main__':
    main()