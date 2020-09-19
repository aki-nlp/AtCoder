import math

def main():
    N = int(input())
    ans = [0]*(N)
    n = int(math.sqrt(N))
    for x in range(1, n+1):
        for y in range(1, n+1):
            for z in range(1, n+1):
                s =x**2 + y**2 + z**2 + x*y + y*z + z*x
                if s < N+1:
                    ans[s - 1] += 1
    for i in ans:
        print(i)
    
if __name__ == '__main__':
    main()