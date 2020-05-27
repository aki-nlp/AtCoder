def main():
    n = int(input())
    s = 2025 - n
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == s:
                print(i, 'x', j, sep=' ')
    
if __name__ == '__main__':
    main()