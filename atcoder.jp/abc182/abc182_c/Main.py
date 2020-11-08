def main():
    n = list(map(int, input()))
    ans = len(n) + 1
    for i in range(2**len(n)):
        su = 0
        cnt = 0
        for j in range(len(n)):
            if ((i >> j) & 1):
                cnt += 1
                su += n[j]
        if su != 0 and su % 3 == 0:
            ans = min(ans, len(n) - cnt)
    if ans == len(n) + 1:
        print(-1)
    else:
        print(ans)
        
if __name__ == '__main__':
    main()
