def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    money = 1000
    have = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            have += money // a[i]
            money -= a[i] * (money // a[i])
        elif a[i] > a[i+1]:
            money += a[i] * have
            have = 0
    money += have * a[-1]
    print(money)
   
    
if __name__ == '__main__':
    main()