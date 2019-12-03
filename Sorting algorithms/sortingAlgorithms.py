import random
import sys
#INSERTION SORT
def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while(i >= 0 and data[i] > key):
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key
    return data

#SELECTION SORT
def selection_sort(toSort):
    for j in range(len(toSort)-1,1,-1):
        max = j
        for i in range(j-1,0,-1):
            if toSort[i]>toSort[max]:
                max = i 
        toSort[j],toSort[max] = toSort[max],toSort[j]


#HEAP SORT
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

#MERGESORT

def merge_sort(toSort):
    temporaryArray = [0]*len(toSort)
    MergeSort(toSort, 0, len(toSort)-1, temporaryArray)
    return toSort

def MergeSort(toSort, left, right, temporaryArray):
    m = (left+right)//2

    if m-left > 0:
        MergeSort(toSort, left, m, temporaryArray)
    if right-m > 1:
        MergeSort(toSort, m+1, right, temporaryArray)
    i=left
    j=m+1
    for k in range(left,right+1,1):
        if (i<=m and j>right) or (i<=m and j<=right and toSort[i]<=toSort[j]):
            temporaryArray[k] = toSort[i]
            i += 1
        else:
            temporaryArray[k] = toSort[j]
            j += 1
    for k in range(left, right+1, 1):
        toSort[k]=temporaryArray[k]

#QUICK SORT RECURSIVE

def quick_sort(data):
    quicksort(data, 0, len(data) - 1)

def quicksort(data, beg, end):
    if beg < end:
        q = partition(data, beg, end)
        quicksort(data, beg, q)
        quicksort(data, q + 1, end)

def partition(data, beg, end):
    x = data[(beg + end) // 2]
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

def quick_sort_right(data):
    sys.setrecursionlimit(15000)

    quicksort_right(data, 0, len(data) - 1)
    #return 0

def quicksort_right(data, beg, end):
    if beg < end:
        q = partition_right(data, beg, end)
        quicksort_right(data, beg, q)
        quicksort_right(data, q + 1, end)

def partition_right(data, beg, end):
    x = data[end]
    i = beg
    j = end
    while True:
        i = i + 1
        j = j - 1

        while(data[j] > x):
            j = j - 1

        while(data[i] < x):
            i = i + 1

        if i < j:
            data[i], data[j] = data[j], data[i]
        else:
            return j

def quick_sort_rand(data):
    quicksort_rand(data, 0, len(data) - 1)

def quicksort_rand(data, beg, end):
    if beg < end:
        q = partition_rand(data, beg, end)
        quicksort_rand(data, beg, q)
        quicksort_rand(data, q + 1, end)

def partition_rand(data, beg, end):
    #print("Random" + str(random.randint(beg, end+1)) + " length: " + str(len(data)))
    x = data[random.randint(beg,end-1)]
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

#QUICKSORT ITERATIVE VERSION
class Record:
    def __init__(self):
        self.l = 0
        self.p = 0

class Stack:
    def __init__(self):
        self.values = []
        
    def push(self, p, l):
        self.values.append((p, l))

    def pop(self):
        return self.values.pop(-1)

    def is_empty(self):
        if len(self.values) > 0:
            return False
        else:
            return True

def init_stack(m):
    stack = []
    for i in range(m):
        stack.append(Record())
    return stack

def quick_sort_i(data):
    m = 12
    stack = Stack()
    stack.push(0, len(data) - 1)
    while True:
        l, p = stack.pop()
        while True:
            i = l
            j = p
            x = data[(l + p) // 2]
            while True:
                while data[i] < x:
                    i = i + 1

                while x < data[j]:
                    j = j - 1

                if i <= j:
                    data[i], data[j] = data[j], data[i]
                    i = i + 1
                    j = j - 1

                if i > j:
                    break

            if i < p:
                stack.push(i, p)
            p = j

            if l >= p:
                break
        if stack.is_empty():
            break

    return data


def quick_sort_i_right(data):
    m = 12
    stack = Stack()
    stack.push(0, len(data) - 1)
    while True:
        l, p = stack.pop()
        while True:
            i = l
            j = p
            x = data[p]
            while True:
                while data[i] < x:
                    i = i + 1

                while x < data[j]:
                    j = j - 1

                if i <= j:
                    data[i], data[j] = data[j], data[i]
                    i = i + 1
                    j = j - 1

                if i > j:
                    break

            if i < p:
                stack.push(i, p)
            p = j

            if l >= p:
                break
        if stack.is_empty():
            break

    return data

def quick_sort_i_rand(data):
    m = 12
    stack = Stack()
    stack.push(0, len(data) - 1)
    while True:
        l, p = stack.pop()
        while True:
            i = l
            j = p
            x = data[random.randint(l,p-1)]
            while True:
                while data[i] < x:
                    i = i + 1

                while x < data[j]:
                    j = j - 1

                if i <= j:
                    data[i], data[j] = data[j], data[i]
                    i = i + 1
                    j = j - 1

                if i > j:
                    break

            if i < p:
                stack.push(i, p)
            p = j

            if l >= p:
                break
        if stack.is_empty():
            break

    return data
