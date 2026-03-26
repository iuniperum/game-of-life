import pygame
import matplotlib
import numpy as np

cell_width = 20
cell_height = 20

class Cell:
    def __init__(self, width, height, state):
        self.width = width
        self.height = height
        self.state = state
    def change_state(self, state, color):
        if (self.state == 1):
            self.state = 0
            self.color = 0
        elif(self.state == 0):
            self.state = 1
            self.color = 1
        else:
            print("ERROR")

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

data = np.random.rand(10, 10) * 20

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [0,10,20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 10, 1));
ax.set_yticks(np.arange(-.5, 10, 1));

plt.show()

'''
pygame.init()

a = int(input("Number of cells horizontal: "))
b = int(input("Number of cells vertical: "))

board = np.zeros((int(a), int(b)))
print(board)

screen = pygame.display.set_mode((a*20, b*20))
pygame.display.set_caption("Conway\'s Game of Life")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
'''