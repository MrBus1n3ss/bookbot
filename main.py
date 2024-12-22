from pathlib import Path

project_root = Path.cwd()
books_dir = project_root / 'books'


def count_characters(words):
    char_count_dict = {}
    for word in words:
        for letter in word.lower():
            if letter not in char_count_dict.keys():
                char_count_dict[letter] = 1
            else:
                char_count_dict[letter] += 1


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
    count_characters(words)


if __name__ == "__main__":
    main()
