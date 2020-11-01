import copy    


def main():
    s = int(input())
    s = str(s)
    a = [0]*10
    for i in s:
        a[int(i)] += 1
        
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
        return
    if len(s) == 2:
        if int(s)%8 ==0 or int(s[1]+s[0])%8==0:
            print('Yes')
        else:
            print('No')
        return
        
    xs = []
    for i in range(1, 500//4):
        x = (500 - i  * 4)*2
        x = str(x).zfill(3)
        if '0' not in x:
            xs.append(x)
#     print(xs)
    
    for x in xs:
        b = copy.copy(a)
        c = [0]*10
        for i in x:
            c[int(i)] += 1
        for i in range(1, 10):
            b[i] -= c[i]
        for i in range(1, 11):
            if i == 10:
                print('Yes')
                return
            if b[i] < 0:
                break
    print('No')
    
        
if __name__ == '__main__':
    main()
