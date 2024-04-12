k = -1
value = 0
d = 1
while d != 0:
    d = int(input())
    move = d
    value += d
    k += 1
if k == 0:
    k = 1
print(value / k)
