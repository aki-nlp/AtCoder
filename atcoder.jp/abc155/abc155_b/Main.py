n = int(input())
a = list(map(int, input().split()))

def judge():
    for i in a:
        if i%2==0:
            if i%3!=0 and i%5!=0:
                return False
    return True

if judge():
    print('APPROVED')
else:
    print('DENIED')