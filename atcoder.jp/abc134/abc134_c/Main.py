def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    b = sorted(a, reverse=True)
    for i in range(n):
        if b[0] !=  a[i]:
            print(b[0])
        else:
            print(b[1])
   
    
if __name__ == '__main__':
    main()