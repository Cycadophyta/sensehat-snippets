from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True

speed = 1

o = (0, 0, 0)
x = (255, 255, 255)

board = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, x, o, o, o,
    o, o, o, o, x, o, o, o,
    o, o, o, o, x, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
]

new_board = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
]


def update_board(board):
    for cell, value in enumerate(board):
        neighbours = count_neighbours(board, cell)
        if value == x:
            if 1 < neighbours < 4:
                new_board[cell] = x
            else:
                new_board[cell] = o
        elif value == o:
            if neighbours == 3:
                new_board[cell] = x
            else: 
                new_board[cell] = o 
    return new_board


def count_neighbours(board, cell):
    count = 0
    for i in [1, 7, 8, 9]:
        if board[(cell + i) % 64] == x: count += 1
        if board[(cell - i) % 64] == x: count += 1
    return count


def main():
    global board, new_board
    generation = 0
    while True:
        sense.set_pixels(board)
        print(f'Generation {generation}')
        new_board = update_board(board)
        board = new_board
        sleep(speed)
        generation += 1


try: 
    main()
except KeyboardInterrupt:
    sense.clear()
