# Difference of max and min floating numbers in a function that can take
# any number of arguments

def checkio(*args):
    if len(args) == 0:
        return 0
    else:
        return max(args) - min(args)
