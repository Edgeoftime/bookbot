def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(text):
    num_words = 0 
    for i in text.split():
        num_words +=1
    return num_words

def main():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    
    print(f"Found {num_words} total words")
    

main()