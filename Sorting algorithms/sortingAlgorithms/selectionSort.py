def selection_sort(toSort):
    for j in range(len(toSort)-1,1,-1):
        max = j
        for i in range(j-1,0,-1):
            if toSort[i]>toSort[max]:
                max = i 
        toSort[j],toSort[max] = toSort[max],toSort[j]
