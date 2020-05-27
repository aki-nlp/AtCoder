def main():
    n = int(input())
    h = list(map(int, input().split()))
    
    pre = h[0]
    for hh in h:
        if hh < pre-1:
            print('No')
            return
        pre = max(pre, hh)
        
    print('Yes')
    
if __name__ == '__main__':
    main()