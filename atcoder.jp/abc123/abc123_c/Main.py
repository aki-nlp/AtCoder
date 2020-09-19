import math

def main():
    n = int(input())             
    a = [int(input()) for _ in range(5)]
    m = min(a)
    print(math.ceil(n/m) + 4)
    
    
if __name__ == '__main__':
    main()