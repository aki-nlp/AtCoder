n = int(input())
x = [len(str(i+1))%2==1 for i in range(n)]
print(sum(x))