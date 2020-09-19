def main():
    a, b, c, d = map(int, input().split())
    candidate = [a*c, a*d, b*c, b*d]
    print(max(candidate))
        
        
if __name__ == '__main__':
    main()