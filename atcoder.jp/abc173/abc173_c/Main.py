import copy
# @patch('builtins.input', test.test_input)
def main():
    h, w, K = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    ans = 0
 
    def get_list(n):
        s = list(range(n))
        n = len(s)
        l = []
        for i in range(2 ** n):
            bit_set = []
            for j in range(n):
                if ((i >> j) & 1):
                    bit_set.append(s[j])
            l.append(bit_set)
        return l
     
    ws = get_list(w)
    hs = get_list(h)
    for wws in ws:
        d = copy.deepcopy(c)
#         print(wws)
        for i in wws:
            for x in range(h):
                d[x][i] = '.'
        e = copy.deepcopy(d)
        for hhs in hs:
            f = copy.deepcopy(e)
            for j in hhs:
                for x in range(w):
                    f[j][x] = '.'
            # print(f)
            tmp = 0
            for x in range(h):
                tmp += f[x].count('#')
            if tmp == K:
                ans += 1
        
    print(ans)
        
    
if __name__ == '__main__':
    main()