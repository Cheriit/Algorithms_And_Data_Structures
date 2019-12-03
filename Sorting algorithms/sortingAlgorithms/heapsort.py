def heap_sort(data):
    build_heap(data)
    heapsize = len(data) -1
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapsize = heapsize - 1
        heapify(data, 0, heapsize)
    return data

def build_heap(data):
    heapsize = len(data) - 1
    for i in range((len(data) - 1) // 2, -1, -1):
        heapify(data, i, heapsize)

def heapify(data, i, heapsize):
    largest = 0
    l = 2 * i + 1
    r = (2 * i) + 2
    if(l <= heapsize and data[l] > data[i]):
        largest = l
    else:
        largest = i

    if(r <= heapsize and data[r] > data[largest]):
        largest = r

    if largest != i:
        data[largest], data[i] = data[i], data[largest]
        heapify(data, largest, heapsize)
