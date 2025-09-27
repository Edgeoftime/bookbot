from stats import number_of_words

def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    
    print(f"Found {num_words} total words")
    

main()