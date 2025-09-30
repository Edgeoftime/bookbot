from stats import number_of_words, get_num_character

def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_char = get_num_character(text)
    num_words = number_of_words(text)
    
    print(f"Found {num_words} total words")
    print(num_char)
    

main()