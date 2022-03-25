import Algorithm_functions as af
import Displaying_functions as df
import pygame

FPS = 1
size = 10

arr = [[1, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 2, 2, 2, 1, 2, 2, 2, 1], [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1, 2], [2, 2, 1, 2, 1, 1, 2, 1, 2, 2],
       [2, 2, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 2, 1, 1], [2, 2, 2, 1, 1, 1, 1, 2, 2, 1],
       [2, 2, 2, 1, 2, 2, 1, 2, 1, 1]]
af.fprint(arr)
tilesize = 50
width = size * tilesize

screen = pygame.display.set_mode((width + 1, width + 1))

df.draw_all_tiles(arr, screen, tilesize, size, width)

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

pygame.init()