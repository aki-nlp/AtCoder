def main():
    a, b =  input().split()
    a = sum(list(map(int, a)))
    b= sum(list(map(int, b)))
    print(max(a, b))

if __name__ == '__main__':
    main()
