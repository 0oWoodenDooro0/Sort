from sort import *

if __name__ == "__main__":
    l = list(range(1, 21))
    shuffle(l)
    print(l)
    radix_msd_sort(l, 2)
    print(l)
