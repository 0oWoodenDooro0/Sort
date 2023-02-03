import time

import pygame

from sort import *

pygame.init()
WIDTH = 1536
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def update(l: list):
    screen.fill((0, 0, 0))
    for i, item in enumerate(l):
        if item < 256:
            color = pygame.Color(255, item, 0)
        elif item < 512:
            color = pygame.Color(511 - item, 255, 0)
        elif item < 768:
            color = pygame.Color(0, 255, item - 512)
        elif item < 1024:
            color = pygame.Color(0, 1023 - item, 255)
        elif item < 1280:
            color = pygame.Color(item - 1024, 0, 255)
        elif item < 1536:
            color = pygame.Color(255, 0, 1535 - item)
        else:
            color = pygame.Color(0, 0, 0)
        pygame.draw.rect(screen, color, pygame.Rect(i, HEIGHT - item * 0.5, 1, item * 0.5))
    pygame.display.update()


if __name__ == '__main__':
    l = list(range(1, 1537))
    update(l)
    time.sleep(1)
    shuffle(l)
    quick_sort(l)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    pygame.quit()
