import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

class Structure:

    def __init__(self, name,directoryName):
        self.name = name
        self.directoryName = directoryName

    def getResults(self, process):
        contentFile = open('./results/'+self.directoryName+'/'+process)
        times = contentFile.read().split()
        return [float(x) for x in times]

class OperationType:

    def __init__(self, name, fileName):
        self.name = name
        self.file = fileName+'.txt'

def drawCharts(operationTypesList, structuresList, scale):
    x = np.linspace(5000, 5000+3000*14, 15)

    for operationType in operationTypesList:
        plt.subplots()
        for struct in structuresList:

            yaxis = struct.getResults(operationType.file)
            yNew = gaussian_filter1d(yaxis, sigma=1.6)
            plt.plot(x, yNew, label=struct.name)

        plt.xlabel('Ilość elementów')
        plt.ylabel('Czas wykonywania operacji [s]')

        plt.title(operationType.name)

        plt.yscale(scale)

        plt.legend(title="Względem klucza:")

        plt.show()


def Main():
    operationTypesList = [
        OperationType('Czas tworzenia struktury','build'),
        OperationType('Czas wyszukiwania wszyskich elementów w strukturze','search'),
        OperationType('Czas usuwania struktury','delete'),
        # OperationType('Wysokość drzewa','height')
    ]

    structuresList = [
        Structure('Drzewo BST','bst'),
        # Structure('Drzewo AVL','avl'),
        Structure('Lista jednokierunkowa','list')

    ]

    drawCharts(operationTypesList, structuresList, 'log')
    
    operationTypesList = [
        OperationType('Wysokość drzewa','height')
    ]

    structuresList = [
        Structure('Drzewo BST','bst'),
        Structure('Drzewo AVL','avl')
    ]

    drawCharts(operationTypesList, structuresList, 'linear')

    


if __name__ == "__main__":
    Main()
