def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    def solve():
        if 0 in a:
            return 0
        ans = 1
        for aa in a:
            ans *= aa
            if ans >10**18:
                return -1
        return ans
    print(solve())
        
    
if __name__ == '__main__':
    main()