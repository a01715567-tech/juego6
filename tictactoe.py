"""Gato (Tic Tac Toe)

Ejercicios

1. Darle a la X y a la O un color y grosor diferente.
2. ¿Qué pasa cuando alguien toca una casilla ocupada?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador controlado por la computadora?

Modificaciones realizadas por Giovanna Tirado Olivera (A01068247):
1. Se cambió el tamaño y el color de los símbolos X y O, y se centraron.
2. Se valida si una casilla ya está ocupada.
3. Se detecta el fin del juego y se indica quién ganó o si hubo empate.
"""

from turtle import *

from freegames import line


def grid():
    """Dibuja la cuadrícula del gato."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el símbolo X del jugador."""
    # Modificación 1: X roja y con línea más gruesa
    color('red')
    width(6)
    # Margen para que la X quede más pequeña y centrada en la casilla
    margin = 30
    line(x + margin, y + margin, x + 133 - margin, y + 133 - margin)
    line(x + margin, y + 133 - margin, x + 133 - margin, y + margin)


def drawo(x, y):
    """Dibuja el símbolo O del jugador."""
    # Modificación 1: O azul y con línea más gruesa
    color('blue')
    width(6)
    radius = 37
    up()
    # circle() dibuja desde el punto más bajo del círculo,
    # por eso se baja el radio para que el centro quede en la casilla
    goto(x + 67, y + 67 - radius)
    down()
    circle(radius)


def floor(value):
    """Redondea el valor hacia abajo a la cuadrícula de casillas de 133."""
    return ((value + 200) // 133) * 133 - 200


# Estado del juego: turno actual (0 = X, 1 = O) y si ya terminó
state = {'player': 0, 'over': False}
players = [drawx, drawo]

# Modificación 2: diccionario con las casillas ocupadas y quién las ocupa
board = {}

# Posiciones posibles de las casillas en cada eje
coords = [-200, -67, 66]


def winner():
    """Modificación 3: regresa el jugador ganador o None si no hay."""
    lines = []
    # Filas y columnas
    for c in coords:
        lines.append([(x, c) for x in coords])
        lines.append([(c, y) for y in coords])
    # Diagonales
    lines.append([(coords[i], coords[i]) for i in range(3)])
    lines.append([(coords[i], coords[2 - i]) for i in range(3)])

    # Si las 3 casillas de una línea son del mismo jugador, ese gana
    for cells in lines:
        values = [board.get(cell) for cell in cells]
        if values[0] is not None and values.count(values[0]) == 3:
            return values[0]
    return None


def show_message(text):
    """Modificación 3: escribe el resultado en el centro del tablero."""
    up()
    goto(0, -20)
    color('green')
    write(text, align='center', font=('Arial', 36, 'bold'))
    print(text)


def tap(x, y):
    """Dibuja X u O en la casilla seleccionada."""
    # Modificación 3: si el juego ya terminó, se ignoran los clics
    if state['over']:
        return

    x = floor(x)
    y = floor(y)

    # Modificación 2: ignora los clics fuera del tablero
    if not (-200 <= x <= 66 and -200 <= y <= 66):
        return

    # Modificación 2: si la casilla ya está ocupada, no se tira
    if (x, y) in board:
        print('Esa casilla ya está ocupada, elige otra.')
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    # Se registra la casilla como ocupada por el jugador actual
    board[(x, y)] = player

    # Modificación 3: revisa si hay ganador o si se llenó el tablero
    win = winner()
    if win is not None:
        name = 'X' if win == 0 else 'O'
        show_message('¡Ganó ' + name + '!')
        state['over'] = True
    elif len(board) == 9:
        show_message('¡Empate!')
        state['over'] = True

    update()
    # Cambia el turno al otro jugador
    state['player'] = not player


# Configuración de la ventana y arranque del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()