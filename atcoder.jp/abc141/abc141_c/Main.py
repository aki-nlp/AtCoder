def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    point = [k - q] * n
    for i in a:
        point[i -1] += 1
    for i in point:
        if i > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()