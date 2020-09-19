def main():
    n, k= map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(1, n-k+1):
        if a[i - 1] < a[k+ i -1]:
            print('Yes')
        else:
            print('No')
            
    
if __name__ == '__main__':
    main()