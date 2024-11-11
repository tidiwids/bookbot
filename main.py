def main():
    book_path = "books/frankenstein.txt"
    file = get_book_text(book_path)
    words = count_words(file)
    characters = count_characters(file)
    print(characters)

def count_characters(text):
    mydic = {}
    for i in text:
        i_lowered = i.lower()
        if i_lowered in mydic:
            mydic[i_lowered] += 1
        else:
            mydic[i_lowered] = 1
    return mydic

def count_words(file):
    words = file.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
