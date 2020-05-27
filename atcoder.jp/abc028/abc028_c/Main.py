def main():
    x = list(map(int, input().split()))
    l = set()
    for a in range(5):
        for b in range(a, 5):
            for c in range(b, 5):
                if a < b < c:
                    l.add(x[a] + x[b] + x[c])
    l = sorted(l)
    print(l[-3])
    
if __name__ == '__main__':
    main()