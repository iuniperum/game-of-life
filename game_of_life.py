import pygame
import numpy as np
import random
import time

cell_width = 20
cell_height = 20

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

def random_population(matrix):
    for cell in range(population):
        i = random.randrange(a - 1)
        j = random.randrange(b - 1)
        while matrix[i][j] == 1:
            i = random.randrange(a - 1)
            j = random.randrange(b - 1)
        print(i, j)
        matrix[i][j] = 1

def grid(matrix, s, x, y):
    for i in range(0, x - 1):
        for j in range(0, y - 1):
            rect = pygame.Rect(i*s, j*s, s, s)
            if(board[i][j] == 1):
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect)


def count_alive(matrix, i, j):
    alive = 0
    for x in range (i - 1, i + 2):
        for y in range (j - 1, j + 2):
            try:
                if x == i and y == j:
                    continue
                if matrix[x][y] == 1:
                    alive += 1
            except:
                pass
    return alive

def determine_state(matrix, x, y):
    for i in range(0, x):
        for j in range(0, y):
            curr_state = matrix[i][j]
            alive_neigh = count_alive(matrix, i, j)
            print(alive_neigh)
            if curr_state == 1 and (alive_neigh < 2 or alive_neigh > 3):
                matrix[i][j] = 0
            if curr_state == 0 and alive_neigh == 3:
                matrix[i][j] = 1

pygame.init()

#a = int(input("Number of cells horizontal: "))
#b = int(input("Number of cells vertical: "))
a = 30
b = 30

size = 1000/a

#population = int(input("Number of alive cells at the start: "))
population = 200

board = np.zeros((int(a), int(b)))
random_population(board)

SCREEN = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Conway\'s Game of Life")

running = True
while running:
    SCREEN.fill(WHITE)
    grid(board, size, a, b)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    new_board = board.copy()
    determine_state(new_board, a, b)
    board = new_board.copy()
    time.sleep(1)
    pygame.display.flip()

pygame.quit()