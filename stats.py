def number_of_words(text):
    num_words = 0 
    for i in text.split():
        num_words +=1
    return num_words