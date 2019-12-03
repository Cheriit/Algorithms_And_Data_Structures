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

    def __init__(self, name, density, fileName):
        self.name = name
        self.density = density
        self.file = density+fileName+'.txt'

def drawCharts(foldersList, filesList, scale):
    x = np.linspace(1000, 1000+1000*14, 15)

    for folder in foldersList:
        plt.subplots()
        for file in filesList:

            yaxis = struct.folder(file.file)
            yNew = gaussian_filter1d(yaxis, sigma=1.6)
            plt.plot(x, yNew, label=struct.name)

        plt.xlabel('Ilość elementów')
        plt.ylabel('Czas wykonywania operacji [s]')

        plt.title(folder.name)

        plt.yscale(scale)

        plt.legend(title="Reprezentacja grafu:")

        plt.show()


def Main():
    foldersList = [
        Folder('Sortowanie topologiczne o gęstości 60%','TS'),
        # Folder('Wyszukiwanie najmniejszego drzewa rozpinającego','Prim'),
    ]

    filesList = [
        # File('Macierz sąsiedztwa','30','Matrix'),
        File('Macierz sąsiedztwa','60','Matrix'),
        # File('Macierz sąsiedztwa','70','Matrix'),
        # File('Lista incydencji','30','Graph'),
        File('Lista incydencji','60','Graph'),
        # File('Lista incydencji','70','Graph'),

    ]

    drawCharts(foldersList, filesList, 'log')
    
    foldersList = [
        # Folder('Sortowanie topologiczne o gęstości 60%','TS'),
        Folder('Wyszukiwanie najmniejszego drzewa rozpinającego dla zagęszczenia 30%','Prim'),
        # Folder('Wyszukiwanie najmniejszego drzewa rozpinającego dla zagęszczenia 70%','Prim'),
    ]

    filesList = [
        File('Macierz sąsiedztwa','30','Matrix'),
        File('Lista incydencji','30','Graph'),

    ]

    drawCharts(foldersList, filesList, 'log')

    foldersList = [
        # Folder('Sortowanie topologiczne o gęstości 60%','TS'),
        # Folder('Wyszukiwanie najmniejszego drzewa rozpinającego dla zagęszczenia 30%','Prim'),
        Folder('Wyszukiwanie najmniejszego drzewa rozpinającego dla zagęszczenia 70%','Prim'),
    ]

    filesList = [

        File('Macierz sąsiedztwa','70','Matrix'),
        File('Lista incydencji','70','Graph'),

    ]

    drawCharts(foldersList, filesList, 'log')

    


if __name__ == "__main__":
    Main()
