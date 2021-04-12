import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# print(board)


# pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)


def draw_lines():
    # 1horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2 horizontal line


pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

# 1 vertical line
pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
# 2 vertical line
pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


print(is_board_full())

# marking all squares

for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        mark_square(row, col, 1)
# board is full - true
print(is_board_full())

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                print(clicked_row)
                print(clicked_col)

            if available_square(clicked_row, clicked_col):
                pygame.display.update()
