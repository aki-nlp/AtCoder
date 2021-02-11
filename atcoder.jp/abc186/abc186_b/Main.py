import numpy as np

def main():
    h, w =  map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(h)]
    x = np.array(x)
    print(np.sum(x - np.min(x)))

                
if __name__ == '__main__':
    main()
