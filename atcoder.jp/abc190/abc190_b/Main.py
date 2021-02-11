def main():
    n, s, d =  map(int, input().split())
    for i in range(n):
        x, y=  map(int, input().split())
        if x < s and d < y:
            print('Yes')
            return
    else:
        print('No')
    
                
if __name__ == '__main__':
    main()