import time
from sort import *
import pygame


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
        pygame.draw.rect(screen, color, pygame.Rect(i * 0.5, HEIGHT - item * 0.5, 1, 1))
    pygame.display.update()


pygame.init()
WIDTH = 768
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
if __name__ == "__main__":
    l = list(range(1, 1537))
    shuffle(l)
