winner = -float('inf')
move = -2
move_old = 0
while move != -1:
    move = int(input())
    if move > move_old:
        winner = move
    move_old = move
print(winner)
