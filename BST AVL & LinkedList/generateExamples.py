import sys
import random
import math

def makeArray(startingSize, stepSize, iterator):

    basicArray = []

    for j in range(int(startingSize)+int(stepSize)*iterator):
        basicArray.append(j)

    return basicArray


def writeArrayToFile(destinationFile, arrayToSave):

    s = str(max(arrayToSave)+1)+'\n'

    for i in arrayToSave:
        s += str(i)+'\n'
    # s=s[:-2]+'\n'

    destinationFile.write(s)


def Main():

    try:
        startingSize = int(sys.argv[1])
        stepSize = int(sys.argv[2])
        destinationFileName = 'arrays.txt'

    except:
        print('Not enough arguments.')

    try:
        destinationFile = open(destinationFileName,"w")
    except:
        print('Falied to create or write file.')
        
    for i in range(15):

        basicArray = makeArray(startingSize, stepSize, i)
        
        random.shuffle(basicArray)
        writeArrayToFile(destinationFile, basicArray)

    destinationFile.close()


if __name__ == "__main__":
    Main()
