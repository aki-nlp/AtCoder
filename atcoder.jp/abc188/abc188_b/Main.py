import numpy as np

def main():
    n =  int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = np.array(a)
    b = np.array(b)
    
    if np.dot(a, b):
        print('No')
    else:
        print('Yes')
                
if __name__ == '__main__':
    main()
