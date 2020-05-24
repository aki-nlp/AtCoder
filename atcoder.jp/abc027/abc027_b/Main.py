n = int(input())
a = list(map(int, input().split()))

def solve():
    if sum(a) % n != 0:
        return -1

    ave = sum(a) // n
    s = 0
    i = 1
    ans = 0
    for x in a:
        s += x
        if s != ave * i:
            ans += 1
            i += 1
        else:
            s = 0
            i = 1
    return ans
    
print(solve())