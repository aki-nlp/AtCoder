def main():
    n, q = map(int, input().split())
    s = input()
    
    t = [0] * n
    pre = s[0]
    t_sum = 0
    for i in range(1, n):
        if pre == 'A' and s[i] == 'C':
            t[i] = t_sum + 1
            t_sum +=  1
        else: 
            t[i] = t_sum
        pre = s[i]
    for _ in range(q):
        l, r = map(int, input().split())
        print(t[r - 1] - t[l - 1])
        
    
if __name__ == '__main__':
    main()