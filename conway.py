import pygame
import sys
from random import randint
from copy import deepcopy

pygame.init()
ROWS = 100
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 8
clock = pygame.time.Clock()
cell = WIDTH // ROWS
W = ROWS
H = ROWS

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

def draw_cell(surface, color, x, y):
    pygame.draw.rect(surface, pygame.Color(color), (x * cell + 2, y * cell + 2, cell - 2, cell - 2))


color = "white"

while True:


    WINDOW.fill(pygame.Color("black"))

    keys = pygame.key.get_pressed()
    colors = ["white", "yellow", "orange", "red", "purple", "blue", "green"]
    
    if keys[pygame.K_RIGHT]:
        if color == "green":
            color = "white"
        else:
            color = colors[colors.index(color) + 1]

    if keys[pygame.K_LEFT]:
        if color == "white":
            color = "green"
        else:
            color = colors[colors.index(color) - 1]

    if keys[pygame.K_UP]:
        if FPS <= 15:
            FPS += 1
    
    if keys[pygame.K_DOWN]:
        if FPS > 1:
            FPS -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                draw_cell(WINDOW, color, x, y)
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    pygame.display.update()
    clock.tick(FPS)

    









