winner = -float('inf')
move = -2
move_old = 0
k = -1
while move != -1:
    move = int(input())
    if move > move_old:
        winner = move
    move_old = move
    k += 1
print(k)
