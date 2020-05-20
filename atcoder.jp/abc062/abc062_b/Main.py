h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

print('#'*(w+2))
for i in a:
    print('#' + ''.join(i) + '#')
print('#'*(w+2))