import sys

def task4():
    file = open(sys.argv[1])
    data = file.read().split('\n')
    file.close
    steps = []
    row = sorted([int(item) for item in data])
    if len(row)%2 == 0:
        median = (row[int(len(row)/2 - 1)] + row[int(len(row)/2)])/2
    else:
        median = row[int(len(row)/2)]
    for item in row:
        steps.append(abs(item - int(median)))
    return sum(steps) 
print(task4())
