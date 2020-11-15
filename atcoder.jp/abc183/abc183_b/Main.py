def main():
    sx, sy, gx, gy = map(int, input().split())
    m = sy
    n = gy
    print((n*sx+m*gx) / (n + m))
        
if __name__ == '__main__':
    main()