import pygame
import numpy as np
import random

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

#def count_neighbourhoods(matrix[i][j])

#def determine_state(matrix, i, j):
#    if (matrix[i][j] )

pygame.init()

#a = int(input("Number of cells horizontal: "))
#b = int(input("Number of cells vertical: "))
a = 300
b = 300

size = 1000/a

#population = int(input("Number of alive cells at the start: "))
population = 100

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

    pygame.display.flip()

pygame.quit()