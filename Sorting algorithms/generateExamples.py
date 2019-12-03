import sys
import random
import math

def makeArray(startingSize, stepSize, iterator):

    basicArray = []

    for j in range(int(startingSize)+int(stepSize)*iterator):
        basicArray.append(j)

    return basicArray


def writeArrayToFile(destinationFile, arrayToSave):

    s = ""

    for i in arrayToSave:
        s += str(i)+', '
    s=s[:-2]+'\n'

    destinationFile.write(s)


def reverseArray(arrayToReverse):

    arrayAfterReverse = []

    for i in arrayToReverse:
        arrayAfterReverse = [i] + arrayAfterReverse
        
    return arrayAfterReverse

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
        centralArrayIndex = math.floor(len(basicArray)/2)

        writeArrayToFile(destinationFile, basicArray)

        basicArray.reverse()
        writeArrayToFile(destinationFile, basicArray)

        random.shuffle(basicArray)
        writeArrayToFile(destinationFile, basicArray)
            
        vArray = sorted(basicArray[:centralArrayIndex], reverse=True)+sorted(basicArray[centralArrayIndex:])
        writeArrayToFile(destinationFile, vArray)
        
        aArray = sorted(basicArray[:centralArrayIndex])+sorted(basicArray[centralArrayIndex:],reverse=True)
        writeArrayToFile(destinationFile, aArray)

            
        writeArrayToFile(destinationFile, [0]*(startingSize+i*stepSize))

    destinationFile.close()


if __name__ == "__main__":
    Main()
