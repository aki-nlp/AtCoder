def main():
    x, y =  map(int, input().split())
    now_lose = min(x, y)
    now_win = max(x, y)
    
    if now_win < now_lose + 3:
        print('Yes')
    else:
        print('No')
    

if __name__ == '__main__':
    main()