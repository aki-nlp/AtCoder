def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    
    ans = [-1]* n
    for s, c in sc:
        s -= 1 
        if ans[s] == -1or ans[s] == c:
            ans[s] = c
        else:
            print(-1)
            return
        
    if ans[0] == -1 and n >1:
        ans[0] = 1
    elif ans[0] == 0:
        if n == 1:
            print(0)
        else:
            print(-1)
        return
    
    print(''.join(list(map(str, ans))).replace('-1', '0'))
    
if __name__ == '__main__':
    main()