def main():
    c = [list(map(int, input().split())) for _ in range(3)]
    s1 = c[0][0] + c[1][1] + c[2][2]
    s2 = c[1][0] + c[2][1] + c[0][2]
    s3 = c[2][0] + c[0][1] + c[1][2]
    s4 = c[0][0] + c[1][2] + c[2][1]
    s5 = c[1][0] + c[2][2] + c[0][1]
    s6 = c[2][0] + c[0][2] + c[1][1]
    
    if s1 == s2 == s3 == s4 == s5 == s6:
        print('Yes')
    else:
        print('No')
    
    
if __name__ == '__main__':
    main()