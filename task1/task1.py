import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def task1():
    index = 1
    while True:
        print(index, end='')
        index = 1 + (index + m - 2) % n
        if index == 1:
            break
print(task1())