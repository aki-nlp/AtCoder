def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

  
def main():
    n = int(input())
    ans = 0 
    zs = []
    f = factorization(n) 
    for p, c in f:
        for i in range(1, c + 1):
            zs.append(p ** i)
    zs = sorted(zs, reverse=True)
    while n >1 and zs != []:
        a = zs.pop()
        if n  % a == 0:
            n = n / a
            ans += 1
    print(ans)
        
            
if __name__ == '__main__':
    main()