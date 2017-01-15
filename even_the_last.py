# Sums even-indexes elements and multiply at the last
    
def checkio(array):
    sum = 0
    if len(array) == 0:
        return 0
    for index, i in enumerate(array):
        if (index % 2 == 0):
            sum += i
    return sum * array[len(array) - 1]
