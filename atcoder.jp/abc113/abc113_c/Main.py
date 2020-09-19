def main():
    n, m = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(m)]
    x = sorted(py, key=lambda x:x[1])
    d = {}
    for p, y in x:
        if type(d.get(p)) != dict:
            d[p]  = {}
        d[p][y] = len(d[p]) + 1
    for p, y in py:
        print('{:0=6}{:0=6}'.format(p, d[p][y]))
         
    
if __name__ == '__main__':
    main()