import itertools

def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    nums = list(range(1, n))
    for i in itertools.permutations(nums):
        time = 0
        before = 0
        for j in i:
            time += t[before][j]
            before = j
        time += t[j][0]
        if time == k:
            ans += 1
            
    print(ans)
    
if __name__ == '__main__':
    main()