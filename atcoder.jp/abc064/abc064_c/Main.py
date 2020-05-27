def main():
    n = int(input())
    a = list(map(int, input().split()))
      
    l = set()    
    free = 0
    for aa in a:
        if aa // 400 >= 8:
            free += 1
        else:
            l.add(aa // 400)
    print(max(1,len(l)), len(l) + free)
        
    
if __name__ == '__main__':
    main()