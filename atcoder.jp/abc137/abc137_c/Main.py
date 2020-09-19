def main():
    n = int(input())
    d = {}
    ans = 0
    
    for _ in range(n):
        ss = ''.join(sorted(input()))
        d[ss] = d.get(ss, 0) + 1
        
    for v in d.values():
            ans += (v*(v-1)) // 2
         
    print(ans)
       
    
if __name__ == '__main__':
    main()