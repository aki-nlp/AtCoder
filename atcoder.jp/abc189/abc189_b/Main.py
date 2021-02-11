def main():
    n, x =  map(int, input().split())
    drunk = 0
    for i in range(n):
        v, p =  map(int, input().split())
        drunk += v * p
        if drunk > x * 100:
            print(i + 1)
            return
    else:
        print(-1)
    
                
if __name__ == '__main__':
    main()
