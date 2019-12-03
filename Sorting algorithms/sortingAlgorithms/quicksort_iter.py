#QUICKSORT ITERATIVE VERSION
import random
class Record:
    def __init__(self):
        self.l = 0
        self.p = 0

def init_stack(m):
    stack = []
    for i in range(m):
        stack.append(Record())
    return stack

def quicksort_i(data):
    m = 12
    stack = init_stack(m)
    #s = random.randint(0, len(data) - 1)
    #s = len(data) - 1
    s = len(data) //2
    stack[0].l = 0
    stack[0].p = len(data) - 1
    while True:
        l = stack[s].l
        p = stack[s].p
        s = s - 1
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
                s = s + 1
                stack[s].l = i
                stack[s].p = p

            p = j

            if l >= p:
                break
        if s == -1:
            break

    return data
