def main():
    h = int(input())
    ans = 0
    i = 0
    while ans < h:
        ans += 2 ** i
        i += 1
    print(ans)
    
      
if __name__ == '__main__':
    main()