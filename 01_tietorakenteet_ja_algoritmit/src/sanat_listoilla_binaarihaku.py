def read_words_to_list(file):
    return file.read().splitlines()


def binary_search(word, list_of_words):
    left = 0
    right = len(list_of_words) - 1

    while left <= right:
        middle = int((left + right) / 2)
        if list_of_words[middle] < word:
            left = middle + 1
        elif list_of_words[middle] > word:
            right = middle - 1
        else:
            return True

    return False


def main():
    finnish_file = open('kotus-sanalista-suomi.txt', encoding='utf-8')
    english_file = open('englanti-UNLICENSED.txt', encoding='utf-8')

    english_words = read_words_to_list(english_file)
    finnish_words = read_words_to_list(finnish_file)

    finnish_file.close()
    english_file.close()

    print(len(finnish_words))
    print(len(english_words))

    count = 0

    for finnish_word in finnish_words:
        if binary_search(finnish_word, english_words):
            print(finnish_word)
            count += 1

    print(f'{count} matches')


main()
