# Find a secret message using uppercase check

def find_message(text):
    result = ""
    for ch in text:
        if ch.isupper() == True:
            result += ch
    return result
