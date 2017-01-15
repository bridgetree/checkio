# Check if a sentence contains three words in succession

def checkio(words):
    count = 0
    for i in words.split():
        if i.isalpha():
            count += 1
            if count == 3:
                return True
                break
        else:
            count = 0
    return False
