def main():
    n = int(input())
    txy = [list(map(int, input().split())) for _ in range(n)]
    
    pre_x, pre_y, pre_t = 0, 0, 0
    for t, x, y in txy:
        d = abs(pre_x - x) + abs(pre_y - y)
        if not(t - pre_t >= d and (t - pre_t) % 2 == d % 2):
            print('No')
            break
        pre_x,  pre_y, pre_t = x, y, t
    else:
        print('Yes')
        
        
if __name__ == '__main__':
    main()