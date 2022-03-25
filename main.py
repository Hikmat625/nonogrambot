import pygame
import Displaying_functions as df
import Algorithm_functions as fn

# 0 in final array means untouched
# 1 in final array means full
# 2 in final array means empty
size = int(input())
rows = []  # input for strings
cols = []  # input for columns

# input arrays

main_arr = [[0 for i in range(size)] for j in range(size)]  # main return array
fn.finput(rows, size)
fn.finput(cols, size)

full_rows = fn.check_for_fulls(rows, size)
full_cols = fn.check_for_fulls(cols, size)

fn.fill_all_full_rows(main_arr, rows, full_rows)
fn.fill_all_full_columns(main_arr, cols, full_cols)
fn.fill_gaps_between_for_1_digit_rows(main_arr, rows)

fn.fprint(main_arr)

FPS = 1
tilesize = 50
width = size * tilesize
screen = pygame.display.set_mode((1000,1000))
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