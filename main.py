from pathlib import Path

project_root = Path.cwd()
books_dir = project_root / 'books'


def count_characters(file_contents):
    char_count_dict = {}
    for letter in file_contents.lower():
        if letter in char_count_dict.keys():
            char_count_dict[letter] += 1
        else:
            char_count_dict[letter] = 1
    return char_count_dict


def count_words(file_contents):
    words = file_contents.split()
    return words, len(words)


def open_book(book):
    with open(Path(books_dir / book)) as file:
        file_contents = file.read()

    return file_contents


def main():
    file_contents = open_book('frankenstein.txt')
    words, word_count = count_words(file_contents)
    char_count_dict = count_characters(file_contents)
    print(char_count_dict['r'])


if __name__ == "__main__":
    main()
