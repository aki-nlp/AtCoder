def main():
    t = input()
    pre = t[0]
    for tt in t:
        if tt=='?':
                print('D', end='')
        else:
            print(tt, end='')
    print()
    
    
if __name__ == '__main__':
    main()