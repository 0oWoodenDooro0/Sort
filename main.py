import random
import time

import pygame


def update(l: list):
    screen.fill((255, 255, 255))
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
        pygame.draw.rect(screen, color, pygame.Rect(i * 0.5, HEIGHT - item * 0.5, 1, item * 0.5))
    pygame.display.update()


def shuffle(target: list):
    l = target[:]
    for i in range(len(target)):
        value = random.choice(l)
        target[i], target[target.index(value)] = value, target[i]
        l.remove(value)
        update(target)
    return target


def selection_sort(target: list):
    for i in range(len(target)):
        minimum_index = i
        for j in range(i, len(target)):
            minimum_index = target.index(min(target[minimum_index], target[j]))
        target[minimum_index], target[i] = target[i], target[minimum_index]
        update(target)
    return target


def bubble_sort(target: list):
    for i in range(len(target)):
        exchange = False
        for j in range(len(target) - 1 - i):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]
                if j % 50 == 0:
                    update(target)
                exchange = True
        update(target)
        if not exchange:
            break
    return target


def insertion_sort(target: list):
    for i in range(1, len(target)):
        k = target[i]
        j = i - 1
        while j >= 0 and target[j] > k:
            j -= 1
        target.remove(k)
        target.insert(j + 1, k)
        update(target)
    return target


def cocktail_shaker_sort(target: list):
    left, right = 0, len(target) - 1
    exchange = True
    while left < right and exchange:
        exchange = False
        for i in range(left, right):
            if target[i] > target[i + 1]:
                target[i], target[i + 1] = target[i + 1], target[i]
                if i % 25 == 0:
                    update(target)
                exchange = True
        update(target)
        right -= 1
        for i in range(right, left, -1):
            if target[i] < target[i - 1]:
                target[i], target[i - 1] = target[i - 1], target[i]
                if i + 12 % 25 == 0:
                    update(target)
                exchange = True
        update(target)
        left += 1
    return target


def merge_sort_in_place(target: list):
    def divide(l: list, left, right):
        if right <= left:
            return
        mid = left + (right - left) // 2
        divide(l, left, mid)
        divide(l, mid + 1, right)
        return merge(l, left, mid, right)

    def merge(l: list, left, mid, right):
        mid += 1
        while left <= mid <= right:
            if l[left] > l[mid]:
                l[left:mid + 1] = [l[mid]] + l[left:mid]
                update(l)
                mid += 1
            else:
                left += 1
        return l

    return divide(target, 0, len(target) - 1)


def merge_sort_out_of_place(target: list):
    def divide(l: list):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        left = divide(left)
        right = divide(right)
        return merge(left, right)

    def merge(left: list, right: list):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.remove(right[0])
            else:
                result.append(left[0])
                left.remove(left[0])
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result

    return divide(target)


pygame.init()
WIDTH = 768
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
l = list(range(1, 1536))
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
merge_sort_in_place(l)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
