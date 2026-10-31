"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(8))*2 # 8 pairs for a 4x4 board
state = {'mark': None, 'pairs': 0}
hide = [True]*16  # 16 tiles

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)  # tile size 
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    
    return int((x+200)//100+((y+200)//100)*4)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""

    return(count % 4)*100-200,(count//4)*100-200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    #Ignore clicks outside the board
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] += 1  # new pair was found



def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

   # Show how many pairs have been found
    up()
    goto(-200, 205)
    color('black')
    write(f"Pares: {state['pairs']} / {len(tiles) // 2}", font=('Arial', 16, 'normal'))

    # All tiles revealed: the game is over
    if not any(hide):
        up()
        goto(0, 0)
        color('red')
        write("¡Ganaste!", align='center', font=('Arial', 40, 'bold'))

    update()

    ontimer(draw, 100)


shuffle(tiles)
setup(420, 480, 370, 0)  # taller window to show the counter
screensize(420, 480)  # drawing area size so the whole board is visible
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

