def main():
    a, b = map(int, input().split())
    c = 2 * a + 100
    print(max(0, c-b))
    
        
if __name__ == '__main__':
    main()