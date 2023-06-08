import sys

def getData(data):
    file = open(data)
    data = file.read().split('\n')
    file.close
    arr = []
    for i in data:
        arr.append(i.split(' '))
    for i in range(len(arr)):
        arr[i] = [float(x) for x in arr[i]]
    return arr


def task2():
    getCirle = getData(sys.argv[1])
    getPoints = getData(sys.argv[2])
    radiusSquared = getCirle[1][0] * getCirle[1][0]
    result = ''
    for point in getPoints:
        equation = (point[0] - getCirle[0][0])**2 + (point[1] - getCirle[0][1])**2
        if equation == radiusSquared:
            result = result + '0\n'
        if equation < radiusSquared:
            result = result + '1\n'
        if equation > radiusSquared:
            result = result + '2\n'
        
    print(result[:-1])

task2()
