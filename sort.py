import random

from show import update


def shuffle(target: list):
    l = target[:]
    for i in range(len(target)):
        value = random.choice(l)
        index = target.index(value)
        target[i], target[index] = value, target[i]
        l.remove(value)
        update(target)
    return target


def swap(l: list, index1, index2):
    l[index1], l[index2] = l[index2], l[index1]


def selection_sort(target: list):
    for i in range(len(target)):
        minimum_index = i
        for j in range(i, len(target)):
            minimum_index = target.index(min(target[minimum_index], target[j]))
        swap(target, minimum_index, i)
        update(target)
    return target


def bubble_sort(target: list):
    for i in range(len(target)):
        exchange = False
        for j in range(len(target) - 1 - i):
            if target[j] > target[j + 1]:
                swap(target, j, j + 1)
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
                swap(target, i, i + 1)
                if i % 25 == 0:
                    update(target)
                exchange = True
        update(target)
        right -= 1
        for i in range(right, left, -1):
            if target[i] < target[i - 1]:
                swap(target, i, i - 1)
                if i + 12 % 25 == 0:
                    update(target)
                exchange = True
        update(target)
        left += 1
    return target


def double_selection_sort(target: list):
    for i in range(len(target) // 2):
        minimum_index = i
        maximum_index = i
        for j in range(i, len(target) - i):
            minimum_index = target.index(min(target[minimum_index], target[j]))
            maximum_index = target.index(max(target[maximum_index], target[j]))
        if target[minimum_index] != target[i]:
            swap(target, minimum_index, i)
            update(target)
        if maximum_index == i:
            maximum_index = minimum_index
        if target[maximum_index] != target[len(target) - i - 1]:
            swap(target, maximum_index, len(target) - i - 1)
            update(target)
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
    def divide(l: list, left_temp=[], right_temp=[]):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        left = divide(left, left_temp=left_temp, right_temp=right + right_temp)
        right = divide(right, left_temp=left_temp + left, right_temp=right_temp)
        result = merge(left, right, left_temp, right_temp)
        return result

    def merge(left: list, right: list, left_temp, right_temp):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right.remove(right[0])
                update(left_temp + result + left + right + right_temp)
            else:
                result.append(left[0])
                left.remove(left[0])
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result

    return divide(target)


def weave_merge_sort(target: list):
    def divide(l: list, left_temp=[], right_temp=[]):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        left = divide(left, left_temp=left_temp, right_temp=right + right_temp)
        right = divide(right, left_temp=left_temp + left, right_temp=right_temp)
        result = merge(left + right, left_temp, right_temp)
        return result

    def merge(l: list, left_temp, right_temp):
        mid = len(l) // 2
        print(l)
        for i in range(mid - 1):
            print(l[mid + i], l[i * 2 + 1:mid + 1], l[mid + i - 1], [l[mid + i]] + l[i * 2: mid - 1])
            l[i * 2], l[i * 2 + 1:mid + 1] = l[mid + i], l[i * 2: mid]
            print(l)
            update(left_temp + l + right_temp)
        for i in range(1, len(l)):
            k = l[i]
            j = i - 1
            while j >= 0 and target[j] > k:
                j -= 1
            l.remove(k)
            l.insert(j + 1, k)
            update(left_temp + l + right_temp)
        return l

    return divide(target)
