def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in s:
        if i == 'o':
            ans += 1
        else:
            ans -= 1
            ans = max(0, ans)
    print(ans)

        
if __name__ == '__main__':
    main()
