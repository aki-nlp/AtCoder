def main():
    n = int(input())
    v = list(map(int, input().split()))
    
    if len(v) == 1:
        return
    
    v = sorted(v, reverse=True)
    ans = (v.pop() + v.pop()) / 2
    
    while v != []:
        v = sorted(v, reverse=True)
        ans = (ans + v.pop()) / 2
        
    print(ans)
    
if __name__ == '__main__':
    main()