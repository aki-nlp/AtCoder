def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcd = [0]*1010
    for i in range(2, 1001):
        for aa in a:
            if aa % i == 0:
                gcd[i] += 1
    print(gcd.index(max(gcd)))
    
        
if __name__ == '__main__':
    main()