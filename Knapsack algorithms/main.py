import random
import sys
import time
from math import floor

#TODO
#Podstawić rozmiar dla zmienych items
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
        if (i<=m and j>right) or (i<=m and j<=right and toSort[i].value/toSort[i].weight>=toSort[j].value/toSort[j].weight):
            temporaryArray[k] = toSort[i]
            i += 1
        else:
            temporaryArray[k] = toSort[j]
            j += 1
    for k in range(left, right+1, 1):
        toSort[k]=temporaryArray[k]

class ItemGenerator:
    def __init__(self, max_value, min_value, max_weight, min_weight):
        self.max_vaule=max_value
        self.min_value=min_value
        self.max_weight=max_weight
        self.min_weight=min_weight

    def generateItemsArray(self, size):
        itemsList = []
        for i in range(size):
            itemsList.append(
                Item(
                    random.randint(self.min_value, self.max_vaule),
                    random.randint(self.min_weight, self.max_weight),
                    i+1
                )
            )
        return itemsList


class Item:
    def __init__(self, value, weight, id):
        self.id = id
        self.value = value
        self.weight = weight

class Knapsack:
    def __init__(self, KnapsackSize, items):
        self.size = KnapsackSize
        self.items = items
        self.itemsSize = len(items)

    def firstFirstUniqueMaxIndex(self, x, y):
        while x > 0:
            if self.optimalMatrix[x][y] != self.optimalMatrix[x-1][y]:
                return x
            x -= 1
        return -1
            # i = 1
            # maxValue = self.optimalMatrix[y_max][x]
            # if maxValue < 1:
            #     return -1
            # while i <= y_max:
            #     if self.optimalMatrix[i][x] == maxValue:
            #         return i
            #     i += 1
        return -1


    def generateOptimalArray(self):
        self.optimalArray = []
        self.generateOptimalMatrix()

        x = self.firstFirstUniqueMaxIndex(self.itemsSize, self. size)
        y = self.size

        while x > 0 and y > 0:
            item = self.items[x-1]
            self.optimalArray.append(item)
            x = self.firstFirstUniqueMaxIndex(x-1, y-item.weight)
            y -= item.weight
            # print(str(x)+" "+str(y))


    def generateOptimalMatrix(self):     #1-Wiersz-Przedmiot, 2-Kolumna-Pojemność
        self.optimalMatrix = []
        for i in range(len(self.items)+1):
            self.optimalMatrix.append([0])

        for i in range(self.size):
            self.optimalMatrix[0].append(0)

        i = 1
        maxVal = 0
        for item in self.items:
            j=1
            while j <= self.size:
                if item.weight <= j:
                    maxVal = self.optimalMatrix[i-1][j-item.weight]+item.value

                    if self.optimalMatrix[i-1][j] > maxVal:
                        maxVal = self.optimalMatrix[i-1][j]

                    self.optimalMatrix[i].append(maxVal)
                else:
                    self.optimalMatrix[i].append(self.optimalMatrix[i-1][j])
                j += 1
            i += 1

    def generateGreedyArray(self):
        self.greedyArray = []
        # itemsList = sorted(self.items, key=lambda x: x.value/x.weight, reverse=True)
        itemsList = merge_sort(self.items)
        for i in itemsList:
            if sum([x.weight for  x in self.greedyArray])+i.weight <= self.size:
                self.greedyArray.append(i)

    def changeItemPool(self, items):
        self.items = items
        self.itemsSize = len(items)

    def changeKnapsackSize(self, size):
        self.size = size

    def print_optimal_matrix(self):
        print("   " + str([i for i in range(self.size+1)]))
        i = 0
        for row in self.optimalMatrix:
            print(str(i) + ": " + str(row))
            i += 1

    def calculateError(self):
        dynamicSum = self.sumValues(self.optimalArray)
        greedySum = self.sumValues(self.greedyArray)

        return ((dynamicSum-greedySum)/dynamicSum)*100

    def sumValues(self, itemList):
        return sum([i.value for i in itemList])

def saveToFile(catalog, filename, array):
    outputFile = open("./results/"+catalog+'/'+filename+'.txt', 'w')
    outputFile.write(str(array)[1:-1])
    outputFile.close()

def print_items(items):
    for item in items:
        print(str(item.id)+" "+str(item.value)+" "+str(item.weight))


def Main():
    itemGenerator = ItemGenerator(20,2,20,2)
    itemList = itemGenerator.generateItemsArray(10)
    knapsack = Knapsack(10, itemList)
    # knapsack.generateGreedyArray()
    # knapsack.generateOptimalArray()
    # knapsack.print_optimal_matrix()
    # print("======================")
    # print_items(knapsack.greedyArray)
    # print("======================")
    # print_items(knapsack.optimalArray)
    capacity = 50
    itemNumber = 40

    optimalChangingItemsTimes = []
    greedyChangingItemsTimes = []

    optimalChangingSizeTimes = []
    greedyChangingSizeTimes = []

    changingItemsError = []
    changingSizeError = []

    knapsack.changeKnapsackSize(capacity)

    progress = 0
    for i in range(15):
        print('Generating results from changing items: '+str(floor(progress/15*100))+'%')
        itemList = itemGenerator.generateItemsArray(itemNumber + itemNumber*i)
        knapsack.changeItemPool(itemList)

        beginOperation = time.time()
        knapsack.generateGreedyArray()
        endOperation = time.time()
        greedyChangingItemsTimes.append(endOperation - beginOperation)

        beginOperation = time.time()
        knapsack.generateOptimalArray()
        endOperation = time.time()
        optimalChangingItemsTimes.append(endOperation - beginOperation)

        changingItemsError.append(knapsack.calculateError())

        progress += 1

    capacity = 10
    itemNumber = 200
    itemList = itemGenerator.generateItemsArray(itemNumber)
    knapsack.changeItemPool(itemList)
    progress = 0
    for i in range(15):
        print('Generating results from changing sizes: '+str(floor(progress/15*100))+'%')
        knapsack.changeKnapsackSize(5+i*capacity)

        beginOperation = time.time()
        knapsack.generateGreedyArray()
        endOperation = time.time()
        greedyChangingSizeTimes.append(endOperation - beginOperation)

        beginOperation = time.time()
        knapsack.generateOptimalArray()
        endOperation = time.time()
        optimalChangingSizeTimes.append(endOperation - beginOperation)

        changingSizeError.append(knapsack.calculateError())
        progress += 1


    saveToFile('times/items', 'dynamic', optimalChangingItemsTimes)
    saveToFile('times/items', 'greedy', greedyChangingItemsTimes)

    saveToFile('times/sizes', 'dynamic', optimalChangingSizeTimes)
    saveToFile('times/sizes', 'greedy', greedyChangingSizeTimes)

    saveToFile('errors/items', 'errors', changingItemsError)
    saveToFile('errors/sizes', 'errors', changingSizeError)


if __name__ == "__main__":
    Main()
