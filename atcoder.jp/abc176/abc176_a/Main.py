import math


def main():
    n, x, t = map(int, input().split())
    print(math.ceil(n / x) * t)
    
if __name__ == '__main__':
    main()