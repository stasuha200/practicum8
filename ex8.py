d = ''
for i in range(1, 10):
    d += str(i)
    print(int(d) * 8 + i)
d = ''
for i in range(1, 10):
    d += str(i)
    print(int(d) * 9 + (i+1))
for i in range(1, 10):
    d = '1' * i
    print(int(d) * int(d))
