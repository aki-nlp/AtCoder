def main():
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        print(1)
    elif n == 1 or m == 1:
        print(max(n, m) - 2)
    else:
        print(n * m - (n + m - 2) * 2)
        
if __name__ == '__main__':
    main()