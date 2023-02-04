from sort import *

if __name__ == "__main__":
    l = list(range(1, 11))
    shuffle(l)
    # l = [8, 0, 6, 3, 7, 4, 5, 1, 2, 9]
    print(l)
    gravity_sort(l)
    print(l)
