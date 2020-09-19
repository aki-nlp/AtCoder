def main():
    x, k, d = map(int, input().split())
    if x >=0 and abs(x) >= k *d:
        print(x - k*d)
    elif x < 0 and abs(x) >= k *d:
        print(abs(x) - k*d)
    else:
        x = abs(x)
        t = x // d
        k -= t
        x -= t*d
        print(abs(x - (k%2)*d))

    
if __name__ == '__main__':
    main()