def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if 0<= i < j < k <= n-1 \
                    and 2 * max([l[i], l[j], l[k]]) < sum([l[i], l[j], l[k]]) \
                    and len(set([l[i], l[j], l[k]]))==3:
                    ans += 1
    print(ans)

    
if __name__ == '__main__':
    main()