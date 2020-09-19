def main():
    a, b, c = map(int, input().split())
    k = int(input())
    
    while k != 0 and a >= b:
        b *= 2
        k -= 1
    while k != 0 and b >= a:
        c *= 2
        k -= 1
    if a < b < c:
        print('Yes')
    else:
        print('No')

    
if __name__ == '__main__':
    main()