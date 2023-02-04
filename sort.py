import random
import time

from main import update


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


def move(l: list, move_index, insert_index):
    value = l[move_index]
    l.remove(value)
    l.insert(insert_index, value)


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
        j = i - 1
        while j >= 0 and target[j] > target[i]:
            j -= 1
        move(target, i, j + 1)
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
                move(l, mid, left)
                update()
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
        for i in range(mid):
            move(l, mid + i, i * 2)
            update(left_temp + l + right_temp)
        for i in range(1, len(l)):
            j = i - 1
            while j >= 0 and l[j] > l[i]:
                j -= 1
            move(l, i, j + 1)
            update(left_temp + l + right_temp)
        return l

    return divide(target)


def quick_sort(target: list):
    def divide(l: list, left, right):
        if left >= right:
            return
        key = l[left]
        i = left
        j = right
        while i != j:
            while l[j] > key and i < j:
                j -= 1
            while l[i] <= key and i < j:
                i += 1
            if i < j:
                swap(l, i, j)
                update(l)
        swap(l, left, i)
        update(l)
        divide(l, left, i - 1)
        divide(l, i + 1, right)

    return divide(target, 0, len(target) - 1)


def max_heap_sort(target: list):
    def heapify(l: list, index, end):
        parent = index
        children = 2 * parent + 1
        if children > end:
            return
        heapify(l, children, end)
        heapify(l, children + 1, end)
        if children + 1 <= end and l[children + 1] > l[children]:
            children += 1
        if l[children] > l[parent]:
            swap(l, parent, children)
            update(l)

    end = len(target) - 1
    while end != 0:
        heapify(target, 0, end)
        swap(target, 0, end)
        update(target)
        end -= 1
    return target


def gravity_sort(target: list):
    index = 0
    count = 0
    breads = target[:]
    result_index = len(target) - 1
    result = target[:]

    while any(breads):
        if breads[index] != 0:
            count += 1
            breads[index] -= 1

        if index == len(target) - 1:
            result[result_index] = count
            result_index -= 1
            update(target)
            index = 0
            count = 0
        else:
            index += 1

    if count != 0:
        result[result_index] = count

    for i in range(len(target) - 1, -1, -1):
        for j in range(len(target) - 1, -1, -1):
            if result[i] < target[j] and i > j:
                target[j] -= 1
            elif target[j] < result[j] and i < j:
                target[j] += 1
        update(target)

    return target


def counting_sort(target: list):
    count = [0] * (max(target) + 1)
    for i in range(len(target)):
        count[target[i]] += 1

    index = 0
    for i in range(len(target)):
        if count[index] == 0:
            index += 1
        if count[index] != 0:
            target[i] = index
            update(target)
            count[index] -= 1


def radix_lsd_sort(target: list, base: int):
    maximum_index = max(target)
    radix = base
    while maximum_index * base // radix != 0:
        bucket = [list() for _ in range(base)]
        for i in range(len(target)):
            bucket[target[i] % radix // (radix // base)].append(target[i])
        index = 0
        result = target[:]
        for i in range(len(target)):
            while not any(bucket[index]):
                if index == base:
                    break
                index += 1
            result[i] = bucket[index].pop(0)
        row = len(result) // base + 1
        for i in range(row):
            for j in range(base):
                if j * row + i >= len(result):
                    break
                target[j * row + i] = result[j * row + i]
            update(target)
        radix *= base
