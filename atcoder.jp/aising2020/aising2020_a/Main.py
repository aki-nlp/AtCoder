def main():
    l, r, d = map(int, input().split())
    a = r // d
    b = (l - 1) // d
    print(a - b)
            
    
if __name__ == '__main__':
    main()