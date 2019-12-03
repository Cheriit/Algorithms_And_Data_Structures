import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

class Folder:

    def __init__(self, name,directoryName):
        self.name = name
        self.directoryName = directoryName

    def getResults(self, filename):
        contentFile = open('./results/'+self.directoryName+'/'+filename)
        times = contentFile.read().split(', ')
        return [float(x) for x in times]

class File:

    def __init__(self, name, fileName):
        self.name = name
        self.file = fileName+'.txt'

def drawCharts(foldersList, filesList, scale, start, step, xdescr):
    x = np.linspace(start, start+step*14, 15)

    for folder in foldersList:
        plt.subplots()
        for file in filesList:

            yaxis = folder.getResults(file.file)
            yNew = gaussian_filter1d(yaxis, sigma=1.6)
            plt.plot(x, yNew, label=file.name)

        plt.xlabel(xdescr)
        plt.ylabel('Czas wykonywania operacji [s]')

        plt.title(folder.name)

        plt.yscale(scale)

        plt.legend(title="Rodzaj algorytmu:")
        plt.savefig('./charts/'+xdescr+'.png')
        plt.show()

def drawBarCharts(foldersList, filesList, start, step):
    x = range(start, start+step*15, step)

    for folder in foldersList:
        objects = ('5','15','25','35','45','55','65','75','85','95','105','115','125','135','145')
        y_pos = np.arange(len(objects))
        yaxis = folder.getResults(filesList[0].file)
        yNew = gaussian_filter1d(yaxis, sigma=1.3)

        plt.figure(figsize=(11,6))
        plt.bar(y_pos, yaxis, align='center', alpha=0.9, width=.8)
        plt.xticks(y_pos, objects)
        plt.ylabel('Błąd w procentach')
        plt.title(folder.name)

        plt.savefig('./charts/' + folder.directoryName + '.png')
        plt.show()


def Main():
    foldersList = [
        Folder('Zajętość czasowa dla problemu plecakowego ze zmienną ilością przedmiotów','times/items'),
        Folder('Zajętość czasowa dla problemu plecakowego ze zmienną pojemnością','times/sizes'),
    ]

    filesList = [
        File('Dynamiczny','dynamic'),
        File('Zachłanny', 'greedy'),

    ]

    drawCharts([foldersList[0]], filesList, 'log', 1000, 1000,'Ilość przedmiotów')
    drawCharts([foldersList[1]], filesList, 'log', 10, 10,'Pojemność')

    foldersList = [
        Folder('Błąd między algorytmami dla zmieniającej się ilości przedmiotów', 'errors/items'),
        Folder('Błąd między algorytmami dla zmieniającej się wielkości plecaka', 'errors/sizes'),
    ]

    filesList = [
        File('Błąd','errors'),
    ]

    drawBarCharts(foldersList, filesList, 1000, 1000)

    


if __name__ == "__main__":
    Main()
