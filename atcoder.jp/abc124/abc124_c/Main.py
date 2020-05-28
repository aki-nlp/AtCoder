def main():
    s = list(map(int, input()))
    
    #startが0
    ans_0 = 0
    #startが1
    ans_1 = 0
    
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != 0:
            ans_0 += 1
        elif i % 2 == 1 and s[i] != 1:
            ans_0 += 1
        if i % 2 == 0 and s[i] != 1:
            ans_1 += 1
        elif i % 2 == 1 and s[i] != 0:
            ans_1 += 1
    print(min(ans_0, ans_1))
        
   
    
if __name__ == '__main__':
    main()