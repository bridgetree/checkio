# Multiply non-zero digits in a number

def checkio(number):
    j = 1
    for i in str(number):
        if i != "0":
            j *= int(i)
    print j
    return j
