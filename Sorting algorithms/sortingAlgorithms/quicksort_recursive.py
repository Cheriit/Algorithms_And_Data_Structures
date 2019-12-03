import random
def quick_sort(data):
    quicksort(data, 0, len(data) - 1)
    return data

def quicksort(data, beg, end):
    if beg < end:
        q = partition(data, beg, end)
        quicksort(data, beg, q)
        quicksort(data, q + 1, end)

def partition(data, beg, end):
    x = data[(beg + end) // 2]
    #x = random.randint(0, len(data) - 1)
    #x = data[0]
    i = beg
    j = end
    while True:
        while(data[j] > x):
            j = j - 1

        while(data[i] < x):
            i = i + 1

        if i < j:
            data[i], data[j] = data[j], data[i]
            i = i + 1
            j = j - 1
        else:
            return j
