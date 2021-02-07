def main():
    a, b, c =  map(int, input().split())
    if a - b > 0:
        print('Takahashi')
    elif b - a > 0:
        print('Aoki')
    else:
        if c == 0:
             print('Aoki')
        else:
             print('Takahashi')

                
if __name__ == '__main__':
    main()