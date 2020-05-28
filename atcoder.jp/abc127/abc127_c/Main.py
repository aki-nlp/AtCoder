def main():
    n, m = map(int, input().split())
    left = 1
    right = n
    for _ in range(m):
        l, r = map(int, input().split())
        left = max(left, l)
        right = min(right, r)
        
    print(max(0, right - left + 1))
   
    
if __name__ == '__main__':
    main()