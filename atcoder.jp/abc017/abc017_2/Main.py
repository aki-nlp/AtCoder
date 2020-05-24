x = input()

def judge(s):
    if s == '':
        return True
    elif s[-1] == 'o' or s[-1] == 'k' or s[-1] == 'u':
        return judge(s[:-1])
    elif s[-2:] == 'ch':
        return judge(s[:-2])
    else:
        return False
if judge(x):
    print('YES')
else:
    print('NO')