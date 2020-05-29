def main():
    s = input()
    k = int(input())
    
    index = 0
    for i, ss in enumerate(s):
        if ss != '1':
            index = i
            break
    
    if k <= index:
        print(1)
    else:
        print(s[index])

if __name__ == '__main__':
    main()