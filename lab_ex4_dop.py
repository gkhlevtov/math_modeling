a = int(input())
for i in range(1, 1000000):
    if a % i == 0:
        print(a // i , i)