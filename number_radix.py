# Base system (return -1 if it's an invalid input)

def checkio(str_number, radix):
    
    try:
        return int(str_number, radix)
    except ValueError:
            return -1
