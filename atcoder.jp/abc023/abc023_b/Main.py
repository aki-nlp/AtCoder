n = int(input())
s = input()

def solve():
    l = len(s)//2
    front = s[:l]
    tail = s[l+1:][::-1]

    if len(s)%2 == 0:
        return -1
    if s[l] != 'b':
        return -1
    for x, y in zip(front, tail):
        z = list('abc')
        if x not in z or y not in z:
            return -1
        if x == 'b':
            if y != 'b':
                return -1
        if x == 'a':
            if y != 'c':
                return -1
        if x == 'c':
            if y != 'a':
                return -1
    return len(front)

print(solve())