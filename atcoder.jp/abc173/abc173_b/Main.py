def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        d[s] = d.get(s, 0) + 1
    
    print('AC x ' + str(d.get('AC', 0)))
    print('WA x ' + str(d.get('WA', 0)))
    print('TLE x ' + str(d.get('TLE', 0)))
    print('RE x ' + str(d.get('RE', 0)))

    
if __name__ == '__main__':
    main()