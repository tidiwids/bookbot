def main():
    book_path = "books/frankenstein.txt"
    file = get_book_text(book_path)
    words = count_words(file)
    characters = count_characters(file)
    cleanup = cleanup_characters(characters)
    print_report(book_path, words, cleanup)

def print_report(book_path, words, characters):
    characters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for i in characters:
        name = i["name"]
        num = i["num"]
        print(f"The '{name}' character was found {num} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def cleanup_characters(chars):
    new_list = []
    new_dic = {}
    for i in chars:
        if i.isalpha():
            new_dic["name"] = i
            new_dic["num"] = chars[i]
            new_list.append(new_dic)
            new_dic = {}
    return new_list

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
