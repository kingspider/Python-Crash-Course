import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

print('Starting desX,desY, X, Y: ' + light_x + ":" + light_y + ":" + initial_tx + ":" + initial_ty


def direction(x, y, dx, dy):
    rdirection = ''

    if y < dy:
        rdirection = rdirection + "N"

        if x < dx:
            rdirection = rdirection + "E"
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            return rdirection
        else:
            return rdirection

    elif y > dy:
        rdirection = rdirection + "S"

        if x < dx:
            rdirection = rdirection + "E"
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            return rdirection
        else:
            return rdirection

    else:

        if x < dx:
            rdirection = rdirection + "E"
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            return rdirection
        else:
            return rdirection


# game loop
while True:
    currentx = 0
    print('currentx: ' + currentx, file=sys.stderr)
    currenty = 0
    print('currenty: ' + currenty, file=sys.stderr)

    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print('remaining turns: ' + remaining_turns, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW

    print(direction(initial_tx, initial_ty, light_x, light_y))
