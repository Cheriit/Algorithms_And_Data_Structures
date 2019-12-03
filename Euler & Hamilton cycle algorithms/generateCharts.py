#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

class Folder:

    def __init__(self, name,directoryName):
        self.name = name
        self.directoryName = directoryName

    def getResults(self, filename):
        contentFile = open('./results/'+self.directoryName+'/'+filename)
        times = contentFile.read().split()
        return [float(x) for x in times]

class File:

    def __init__(self, name, fileName):
        self.name = name
        self.file = fileName

def drawCharts(foldersList, filesList, scale, legendTitle):
    x = np.linspace(6, 6+1*10, 11)

    for folder in foldersList:
        plt.subplots()
        for file in filesList:

            yaxis = folder.getResults(file.file)
            yNew = gaussian_filter1d(yaxis, sigma=1.6)
            plt.plot(x, yNew, label=file.name)

        plt.xlabel('Ilość wierzchołków')
        plt.ylabel('Czas pracy [s]')

        plt.title(folder.name)

        plt.yscale(scale)

        plt.legend(title=legendTitle)

        plt.show()


def Main():
    # foldersList = [
    #     Folder('Zajętość czasowa dla algorytów poszukujących w grafach o nasyceniu 30%','30'),
    #     Folder('Zajętość czasowa dla algorytów poszukujących w grafach o nasyceniu 70%','70'),
    # ]

    # filesList = [
    #     File('Cykl Eulera','euler'),
    #     File('Cykl Hamiltona', 'hamilton'),
    # ]

    # drawCharts(foldersList, filesList, 'log','Alg. szukania:')
    foldersList = [
        Folder('Zajętość czasowa dla algorytmu poszukającego wszystkich cyklów Hamiltona:', 'HamiltonAll'),
    ]
    filesList = [
        File('50%', '50')
    ]

    drawCharts(foldersList, filesList, 'log',"Gęstość grafu:")



if __name__ == "__main__":
    Main()
