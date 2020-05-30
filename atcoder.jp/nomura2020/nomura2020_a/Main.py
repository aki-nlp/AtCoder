def main():
    h1, m1, h2, m2, k = map(int, input().split())
    
    h = h2 - h1
    m = h * 60 + m2 - m1 - k
    print(m)
    
   
    
if __name__ == '__main__':
    main()