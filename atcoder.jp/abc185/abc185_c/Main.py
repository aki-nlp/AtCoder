import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

  
def main():
    l = int(input())
    print(combinations_count(l - 1, 11))
    
                
if __name__ == '__main__':
    main()
