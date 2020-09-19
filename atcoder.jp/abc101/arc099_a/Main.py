import math


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(math.ceil((n -1) / (k - 1)))

    
if __name__ == '__main__':
    main()