def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s[0] == '!':
            if d.get(s[1:], 0) > 0:
                print(s[1:])
                return
            else:
                d[s[1:]] = -1
        else:
            if d.get(s, 0) < 0:
                print(s)
                return
            else:
                d[s] = 1
    else:
        print('satisfiable')
    
                
if __name__ == '__main__':
    main()