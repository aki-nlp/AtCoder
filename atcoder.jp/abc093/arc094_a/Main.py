def main():
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    d = m * 3 - sum([a, b, c])
    ans = d // 2
    if d % 2 == 0:
        print(ans)
    else:
        print(ans + 2)
    
if __name__ == '__main__':
    main()