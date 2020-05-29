def main():
    s = input()
    a = s.count('0')
    b = s.count('1')
    print(len(s) - abs(a - b))       

if __name__ == '__main__':
    main()