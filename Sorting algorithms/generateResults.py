import time
import sys
import sortingAlgorithms as sort

class DataContainer:

    def __init__(self):
        self.incremental = []
        self.decremental = []
        self.shuffled = []
        self.vShaped = []
        self.aShaped = []
        self.constant = []

        
class SortingAlgorithm:

    def __init__(self, name, sortingFunction ):
        self.name = name
        self.fileName = name + '.txt'
        self.sortingFunction = sortingFunction
        self.incrementalTimes = []
        self.decrementalTimes = []
        self.vShapedTimes = []
        self.aShapedTimes = []
        self.shuffledTimes = []
        self.constantTimes = []

    def sortArray(self, originalArray):
        arrayToSort = [int(x) for x in originalArray]
        beginOperation= time.time()
        self.sortingFunction(arrayToSort)
        endOperation = time.time()
        return endOperation-beginOperation
    
    def pushTimes(self, timesArray):
        self.incrementalTimes.append(timesArray[0])
        self.decrementalTimes.append(timesArray[1])
        self.vShapedTimes.append(timesArray[2])
        self.shuffledTimes.append(timesArray[3])
        self.aShapedTimes.append(timesArray[4])
        self.constantTimes.append(timesArray[5])



def sortData(dataArrays, sortingAlgorithmsList):
    for algorithm in sortingAlgorithmsList:
        times = [[],[],[],[],[],[]]

        for i in range(3):
            #times[0].append(algorithm.sortArray(dataArrays.incremental))
            #times[1].append(algorithm.sortArray(dataArrays.decremental))
            #times[2].append(algorithm.sortArray(dataArrays.vShaped))
            times[3].append(algorithm.sortArray(dataArrays.shuffled))
            times[4].append(algorithm.sortArray(dataArrays.aShaped))
            #times[5].append(algorithm.sortArray(dataArrays.constant))

        algorithm.pushTimes([sum(x)/3.0 for x in times])
        
def writeToFile(algorithms):
    for alg in algorithms:
        # resultFile = open("./results/incremental/"+alg.fileName,'w')
        # resultFile.write(str(alg.incrementalTimes)[1:-1])

        # resultFile = open("./results/decremental/"+alg.fileName,'w')
        # resultFile.write(str(alg.decrementalTimes)[1:-1])

        resultFile = open("./results/shuffled/"+alg.fileName,'w')
        resultFile.write(str(alg.shuffledTimes)[1:-1])

        # resultFile = open("./results/vshaped/"+alg.fileName,'w')
        # resultFile.write(str(alg.vShapedTimes)[1:-1])

        resultFile = open("./results/aShaped/"+alg.fileName,'w')
        resultFile.write(str(alg.aShapedTimes)[1:-1])

        # resultFile = open("./results/constant/"+alg.fileName,'w')
        # resultFile.write(str(alg.constantTimes)[1:-1])
        

def Main():
    


    sortingAlgorithmsList = [
    # SortingAlgorithm('insertion', sort.insertion_sort),
    # SortingAlgorithm('selection', sort.selection_sort),
    # SortingAlgorithm('heap', sort.heap_sort),
    # SortingAlgorithm('merge',sort.merge_sort),
    SortingAlgorithm('quick_sort', sort.quick_sort),
    SortingAlgorithm('quick_sort_right', sort.quick_sort_right),
    SortingAlgorithm('quick_sort_rand', sort.quick_sort_rand),
    SortingAlgorithm('quick_sort_i', sort.quick_sort_i),
    SortingAlgorithm('quick_sort_i_right', sort.quick_sort_i_right),
    SortingAlgorithm('quick_sort_i_rand', sort.quick_sort_i_rand)
    ]
    
    dataArrays = DataContainer()

    try:
        dataFile = open('arrays.txt',"r")
    except:
        print('File doesn\'t exist')


    for step in range(15):

        dataArrays.incremental = dataFile.readline().split(", ")
        dataArrays.decremental = dataFile.readline().split(", ")
        dataArrays.shuffled = dataFile.readline().split(", ")
        dataArrays.vShaped = dataFile.readline().split(", ")
        dataArrays.aShaped = dataFile.readline().split(", ")
        dataArrays.constant = dataFile.readline().split(", ")


        sortData(dataArrays,sortingAlgorithmsList)
        print('Progress: '+str((step+1)/15*100)+'%')



       
    writeToFile(sortingAlgorithmsList)
        

if __name__ == "__main__":
    Main()
