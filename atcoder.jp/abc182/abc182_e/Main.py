import copy    

def main():
    h, w, n, m = map(int, input().split())
    field = [[0 for _ in range(w)] for _ in range(h)]
    for _  in range(n):
        x, y = map(int, input().split())
        field[x-1][y-1] = 2
    for _  in range(m):
        x, y = map(int, input().split())
        field[x-1][y-1] = -1
        
    field2 = copy.deepcopy(field)
    
    for i in range(h):
        for j in range(w):
            if field[i][j] == 2:
                # right
                k = j + 1
                while k < w:
                    if field[i][k] == -1 or  field[i][k] == 1:
                        break
                    else:
                        field[i][k] = max(1, field[i][k])
                    k += 1
                    
                # left
                k = j - 1
                while k >= 0:
                    if field[i][k] == -1 or  field[i][k] == 1:
                        break
                    else:
                        field[i][k] = max(1, field[i][k])
                    k -= 1
                
    for i in range(h):
        for j in range(w):
            if field2[i][j] == 2:
                # down
                k = i + 1
                while k < h:
                    if field2[k][j] == -1 or  field2[k][j] == 1:
                        break
                    else:
                        field2[k][j] = max(1, field2[k][j])
                    k += 1
                
                # up
                k = i - 1
                while k >= 0:
                    if field2[k][j] == -1 or  field2[k][j] == 1:
                        break
                    else:
                        field2[k][j] = max(1, field2[k][j])
                    k -= 1
                
    ans = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] + field2[i][j] >=1:
                ans += 1
    print(ans)

    
        
if __name__ == '__main__':
    main()
