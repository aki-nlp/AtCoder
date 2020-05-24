s = input()
pre = s[0]
count = 0
for i in s:
    if i == pre:
        count += 1
    else:
        print(pre+str(count), end='')
        count = 1
        pre = i
print(pre+str(count))