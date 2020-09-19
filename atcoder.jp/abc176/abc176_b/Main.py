def main():
    n = list(map(int, input()))
    if sum(n)%9 == 0:
        print('Yes')
    else:
        print('No')
        
        
if __name__ == '__main__':
    main()