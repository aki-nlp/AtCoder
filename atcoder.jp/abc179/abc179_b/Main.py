def main():
    n = int(input())
    count = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a == b:
            count +=1
            if count == 3:
                print('Yes')
                return
        else:
            count = 0
    else:
        print('No')

        
if __name__ == '__main__':
    main()