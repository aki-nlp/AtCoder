def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    y = []
    s = x[m - 1] - x[0]
    for i in range(1, m):
        y.append(x[i] - x[i - 1])
    y = sorted(y, reverse=True)
    m = sum(y[0: n - 1])
    print(s - m)
    
if __name__ == '__main__':
    main()