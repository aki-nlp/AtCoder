def main():
    n = int(input())
    a = list(map(int, input().split()))
      
    b = [0] * (10**6)
    for aa in a:
        b[aa - 1] += 1 
        b[aa + 0] += 1 
        b[aa + 1] += 1 
        
    print(max(b))
        
    
if __name__ == '__main__':
    main()