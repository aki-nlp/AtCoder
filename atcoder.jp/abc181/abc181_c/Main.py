def check(ab, n):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = ab[i]
                x2, y2 = ab[j]
                x3, y3 = ab[k]
                u1, v1 = x2 - x1, y2 - y1
                u2, v2 = x3 - x1, y3 - y1
                if u1*v2 == v1*u2:
                    return True
    return False
            

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    if check(ab, n):
        print('Yes')
    else:
        print('No')
    
        
if __name__ == '__main__':
    main()