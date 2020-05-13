s = input()
a = ['R', 'U', 'D']
b = ['L', 'U', 'D']

def judge():
    for i in range(len(s)):
        if i%2==0 and s[i] not in a:
            return False
        if i%2==1 and s[i] not in b:
            return False
    return True

if judge():
    print('Yes')
else:
    print('No')