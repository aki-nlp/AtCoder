def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def main():
    n = int(input())
    ans = sorted(divisor(n))
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
