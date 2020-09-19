def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    
    def judge(y, x):
        if s[y][x] == '.':
            return True
        for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ny = y + dy
            nx = x + dx
            if 0<= ny < h and 0<= nx < w:
                if s[ny][nx] == '#':
                    return True
        return False
            
        
    for y in range(h):
        for x in range(w):
            if judge(y, x) == False:
                print('No')
                return
    else:
        print('Yes')
        
        
if __name__ == '__main__':
    main()