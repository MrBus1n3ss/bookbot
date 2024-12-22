from pathlib import Path

project_root = Path.cwd()
books_dir = project_root / 'books'


def count_characters(file_contents):
    char_count_dict = {}
    for letter in file_contents.lower():
        if letter.isalpha():
            if letter in char_count_dict.keys():
                char_count_dict[letter] += 1
            else:
                char_count_dict[letter] = 1
    return char_count_dict


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def open_book(book):
    with open(Path(books_dir / book)) as file:
        file_contents = file.read()
    return file_contents


def convert_char_count_to_list(char_count_dict):
    char_count_list = []
    for k, v in char_count_dict.items():
        char_count_list.append({'letter': k, 'count': v})
    return char_count_list


def sort_on(dict):
    return dict['count']


def create_report(word_count, char_count_list, book):
    print(f'--- Begin report of books/{book} ---')
    print(f'{word_count} words found in the document')
    for item in char_count_list:
        letter = item['letter']
        count = item['count']
        print(f"The '{letter}' was found {count} times")
    print('--- End report ---')


def main():
    file_contents = open_book('frankenstein.txt')
    word_count = count_words(file_contents)
    char_count_dict = count_characters(file_contents)
    char_count_list = convert_char_count_to_list(char_count_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    create_report(word_count, char_count_list, 'frankenstein.txt')


if __name__ == "__main__":
    main()
