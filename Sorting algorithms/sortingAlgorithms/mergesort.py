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
