import Algorithm_functions as al
import Displaying_functions as df
import pygame

# 0 in final array means untouched
# 1 in final array means full
# 2 in final array means empty
size = int(input())
rows = []  # input for strings
cols = []  # input for columns

# input arrays

main_arr = [[0 for i in range(size)] for j in range(size)]  # main return array
al.finput(rows, size)
al.finput(cols, size)

full_rows = al.check_for_fulls(rows, size)
full_cols = al.check_for_fulls(cols, size)

al.fill_all_full_rows(main_arr, rows, full_rows)
al.fill_all_full_columns(main_arr, cols, full_cols)
al.bottom_guided_columns(main_arr, cols)
# fn.top_guided_columns(main_arr,cols)
# fn.left_guided_rows(main_arr,cols)
"""al.testver(main_arr, rows)
al.testver(main_arr, rows)
al.testver(main_arr, rows)"""

al.fprint(main_arr)

FPS = 1
tilesize = 50
width = size * tilesize
screen = pygame.display.set_mode((width+1,width+1))
clock = pygame.time.Clock()
finished = False

df.draw_all_tiles(main_arr,screen,tilesize,size,width)
pygame.display.update()


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

pygame.init()
