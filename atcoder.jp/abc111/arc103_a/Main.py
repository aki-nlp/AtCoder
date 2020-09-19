import collections

def main():
    n = int(input())
    v = list(map(str, input().split()))

    c1 = collections.Counter(v[0::2])
    c2 = collections.Counter(v[1::2])
    
    def most(c, x, y):
        return c.most_common()[x][y]
    
    if most(c1, 0, 1) == most(c2, 0, 1) == n//2 and most(c1, 0, 0) == most(c2, 0, 0):
        print(n // 2)
    elif most(c1, 0, 0) != most(c2, 0, 0):
        print(n - most(c1, 0, 1)- most(c2, 0, 1))
    else:
            a  = n - most(c1, 1, 1)- most(c2, 0, 1)
            b  = n - most(c1, 0, 1)- most(c2, 1, 1)
            print(min(a, b))
         
    
if __name__ == '__main__':
    main()