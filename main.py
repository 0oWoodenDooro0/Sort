import pygame
from sort import *
import time

l = list(range(1, 1537))
update(l)
time.sleep(1)
shuffle(l)
selection_sort(l)
shuffle(l)
bubble_sort(l)
shuffle(l)
insertion_sort(l)
shuffle(l)
cocktail_shaker_sort(l)
shuffle(l)
double_selection_sort(l)
shuffle(l)
merge_sort_in_place(l)
shuffle(l)
merge_sort_out_of_place(l)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
