def main():
    n, m, t = map(int, input().split())
    battery = n
    flag = True
    now = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        battery -= a - now
        if battery <=  0:
            flag = False
        battery += b - a
        battery = min( battery, n)
        now = b

    if battery - (t - now) <=  0:
        flag = False

    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
