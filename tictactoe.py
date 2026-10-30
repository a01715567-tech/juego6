"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('red')
    width(6)
    margin = 30
    line(x + margin, y + margin, x + 133 - margin, y + 133 - margin)
    line(x + margin, y + 133 - margin, x + 133 - margin, y + margin)


def drawo(x, y):
    """Draw O player."""
    color('blue')
    width(6)
    radius = 37
    up()
    goto(x + 67, y + 67 - radius)
    down()
    circle(radius)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0, 'over': False}
players = [drawx, drawo]
board = {}
coords = [-200, -67, 66]


def winner():
    """Return the winning player or None."""
    lines = []
    for c in coords:
        lines.append([(x, c) for x in coords])
        lines.append([(c, y) for y in coords])
    lines.append([(coords[i], coords[i]) for i in range(3)])
    lines.append([(coords[i], coords[2 - i]) for i in range(3)])

    for cells in lines:
        values = [board.get(cell) for cell in cells]
        if values[0] is not None and values.count(values[0]) == 3:
            return values[0]
    return None


def show_message(text):
    """Write the final result in the middle of the board."""
    up()
    goto(0, -20)
    color('green')
    write(text, align='center', font=('Arial', 36, 'bold'))
    print(text)


def tap(x, y):
    """Draw X or O in tapped square."""
    if state['over']:
        return

    x = floor(x)
    y = floor(y)

    if not (-200 <= x <= 66 and -200 <= y <= 66):
        return

    if (x, y) in board:
        print('Esa casilla ya está ocupada, elige otra.')
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[(x, y)] = player

    win = winner()
    if win is not None:
        name = 'X' if win == 0 else 'O'
        show_message('¡Ganó ' + name + '!')
        state['over'] = True
    elif len(board) == 9:
        show_message('¡Empate!')
        state['over'] = True

    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
