from sort import *

if __name__ == "__main__":
    l = list(range(10))
    shuffle(l)
    l = [2, 4, 3, 8, 5, 9, 7, 6, 1, 0]
    print(l)
    quick_sort(l)
    print(l)
