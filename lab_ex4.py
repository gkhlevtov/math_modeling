a = int(input())
i = 0
c = 1
b = 1
print(c, end=' ')
print(c, end=' ')
while i < a-1:
    d = b + c
    print(d, end=' ')
    b = c
    c = d
    i += 1
