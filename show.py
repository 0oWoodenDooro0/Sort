from sort import *

if __name__ == "__main__":
    l = list(range(1, 21))
    shuffle(l)
    print(l)
    radix_lsd_in_place_sort(l, 10)
    print(l)
