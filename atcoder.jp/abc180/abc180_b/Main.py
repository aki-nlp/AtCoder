import math


def main():
    n = int(input())
    x = list(map(int, input().split()))
    
    manhattan = sum(list(map(lambda i: abs(i), x)))
    euclid = math.sqrt(sum(list(map(lambda i: abs(i)**2, x))))
    chebyshev = max(list(map(lambda i: abs(i), x)))
    
    print(manhattan)
    print(euclid)
    print(chebyshev)

        
if __name__ == '__main__':
    main()
