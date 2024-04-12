n = int(input())
for i in range(2, n+1):
    s = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            s += 1
    if s == 0:
        print(i)
