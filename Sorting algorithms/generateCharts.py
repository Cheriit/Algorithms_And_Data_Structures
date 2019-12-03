import matplotlib.pyplot as plt
import numpy as np

class SortingAlgorithm:

    def __init__(self, name, fileName, description):
        self.name = name
        self.fileName = fileName + '.txt'
        self.description = description


    def getResults(self, catalog):
        contentFile = open('./results/'+catalog+'/'+self.fileName)
        times = contentFile.read().split(', ')
        return [float(x) for x in times]

class DataType:

    def __init__(self, name, catalog, description):
        self.name = name
        self.catalog = catalog
        self.description = description



def Main():
    dataTypesList = [
        # DataType('Stałe','constant','Tablice stałych wartości:'),
        # DataType('Rosnące','incremental','Tablice rosnących wartości:'),
        # DataType('Malejące','decremental','Tablice malejących wartości:'),
        # DataType('Losowe','shuffled','Tablice losowych wartości:'),
        # DataType('Litera V','vshaped','Tablice wartości w kształcie litery \"V\" :'),
        DataType('Litera A','aShaped','Tablice wartości w kształcie litery \"A\" Quicksort\'a rekurencyjnego:')

    ]

    sortingAlgorithmsList = [
        #SortingAlgorithm('Selectionsort','selection','Sortowanie algorytmem Selection Sort'),
        #SortingAlgorithm('Insertionsort','insertion','Sortowanie algorytmem Insertion Sort'),
        #SortingAlgorithm('Heapsort','heap','Sortowanie algorytmem Heap Sort'),
        #SortingAlgorithm('Mergesort','merge','Sortowanie algorytmem Merge Sort'),
        SortingAlgorithm('Skrajnie prawy','quick_sort_right','Sortowanie algorytmem Quick Sort (rekurencyjny)'),
        SortingAlgorithm('Środkowy','quick_sort','Sortowanie algorytmem Quick Sort (rekurencyjny)'),
        SortingAlgorithm('Losowy','quick_sort_rand','Sortowanie algorytmem Quick Sort (rekurencyjny)'),
        # SortingAlgorithm('Quicksort it.','quick_sort_i','Sortowanie algorytmem Quick Sort (iteracyjny)'),


    ]

    x = np.linspace(1000, 1000+1000*14, 15)

    for dataType in dataTypesList:
        plt.subplots()
        for alg in sortingAlgorithmsList:

            yaxis = alg.getResults(dataType.catalog)
            # print(yaxis)
            plt.plot(x, yaxis, label=alg.name)

        plt.xlabel('Ilość elementów')
        plt.ylabel('Czas sortowania [s]')

        plt.title(dataType.description )

        plt.yscale('log')

        plt.legend(title="Względem klucza:")

        plt.show()
        
    for alg in sortingAlgorithmsList:
        plt.subplots()
        
        for dataType in dataTypesList:
            yaxis = alg.getResults(dataType.catalog)
            plt.plot(x, yaxis, label=dataType.name)
        
        plt.xlabel('Ilość elementów')
        plt.ylabel('Czas sortowania [s]')
        plt.yscale('log')
        plt.legend(title="Typ danych")
        plt.show()


if __name__ == "__main__":
    Main()
