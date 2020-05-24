n = int(input())
d = [int(input()) for _ in range(n)]
print(len(d)-len(set(d)))