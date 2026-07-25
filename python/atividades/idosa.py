
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 6
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 12
SPACE = SQUARE_SIZE // 4

BG_COLOR = (245, 245, 245)
LINE_COLOR = (50, 50, 50)
CIRCLE_COLOR = (30, 144, 255)
CROSS_COLOR = (220, 20, 60)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 1
game_over = False

def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                    CROSS_WIDTH,
                )

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0

def board_full():
    return all(board[r][c] != 0 for r in range(3) for c in range(3))

screen.fill(BG_COLOR)
draw_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            if board[row][col] == 0:
                board[row][col] = player

                winner = check_winner()
                if winner or board_full():
                    game_over = True
                    print("Fim de jogo! Vencedor:", "O" if winner == 1 else "X" if winner == 2 else "Empate")
                else:
                    player = 2 if player == 1 else 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            board = [[0 for _ in range(3)] for _ in range(3)]
            player = 1
            game_over = False

    screen.fill(BG_COLOR)
    draw_grid()
    draw_figures()
    pygame.display.update()
