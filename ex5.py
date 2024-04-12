n = int(input())
k = 0
for i in range(2, n+1):
    s = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            s = s + j + (i / j)
    if s == i:
        k += 1
print(k)
