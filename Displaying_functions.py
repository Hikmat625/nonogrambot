import pygame

gray = (60, 60, 60)


def grid(size, width, screen, tilesize):
    for i in range(size + 1):
        if i-1%5==0:
            pygame.draw.line(screen, "white", (0, tilesize * i), (width, tilesize * i), 3)
            pygame.draw.line(screen, "white", (tilesize * i, 0), (tilesize * i, width), 3)
        else:
            pygame.draw.line(screen, "white", (0, tilesize * i), (width, tilesize * i), 1)
            pygame.draw.line(screen, "white", (tilesize * i, 0), (tilesize * i, width), 1)


def full_tile(screen, xcor, ycor, tilesize):
    rectangle = pygame.Rect((xcor * tilesize + 1, ycor * tilesize + 1), (tilesize - 1, tilesize - 1))
    pygame.draw.rect(screen, gray, rectangle, 0)


def x_tile(screen, xcor, ycor, tilesize):
    pygame.draw.line(screen, gray, (xcor * tilesize + 1, ycor * tilesize + 1),
                     ((xcor + 1) * tilesize, (ycor + 1) * tilesize), 4)
    pygame.draw.line(screen, gray, ((xcor + 1) * tilesize, ycor * tilesize + 1),
                     (xcor * tilesize + 1, (ycor + 1) * tilesize), 4)


def draw_all_tiles(arr, screen, tilesize, size, width):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                full_tile(screen, j, i, tilesize)
            if arr[i][j] == 2:
                x_tile(screen, j, i, tilesize)
    grid(size, width, screen, tilesize)
