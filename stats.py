def number_of_words(text):
    num_words = 0 
    for i in text.split():
        num_words +=1
    return num_words

def get_num_character(text):
    num_char = {}
    for c in text:
        lowered = c.lower()
        if lowered in num_char:
            num_char[lowered] += 1 
        else:
            num_char[lowered] = 1
    return num_char