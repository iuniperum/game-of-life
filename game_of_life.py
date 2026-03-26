import pygame
import matplotlib
import numpy as np

cell_width = 20
cell_height = 20

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

class Cell:
    def __init__(self, width, height, state):
        self.width = width
        self.height = height
        self.state = state
    def change_state(self, state, color):
        if (self.state == 1):
            self.state = 0
            self.color = pygame.Color('white')
        elif(self.state == 0):
            self.state = 1
            self.color = pygame.Color('black')
        else:
            print("ERROR")

#def count_neighbourhoods(matrix[i][j])

#def determine_state(matrix, i, j):
#    if (matrix[i][j] )

pygame.init()

#a = int(input("Number of cells horizontal: "))
#b = int(input("Number of cells vertical: "))
a = 30
b = 30

board = np.zeros((int(a), int(b)))
board[15, 15] = 1
board[15, 16] = 1
board[14, 16] = 1
board[16, 16] = 1
board[15, 17] = 1
print(board)

def grid(matrix):
    size = 20
    for x in range(0, a, size):
        for y in range(0, b, size):
            rect = pygame.Rect(x*size, y*size, size, size)
            if(board[x][y] == 1):
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect)

SCREEN = pygame.display.set_mode((a*20, b*20))
pygame.display.set_caption("Conway\'s Game of Life")

running = True
while running:
    SCREEN.fill(WHITE)
    grid(board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()