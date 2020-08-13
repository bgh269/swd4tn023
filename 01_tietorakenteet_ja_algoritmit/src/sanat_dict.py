
def read_words_to_dict(file):
    words = dict()
    for line in file:
        word = line.strip()
        words[word] = True
    return words

def main():
    finnish_file = open('kotus-sanalista-suomi.txt', encoding='utf-8')
    english_file = open('englanti-UNLICENSED.txt', encoding='utf-8')

    english_words = read_words_to_dict(english_file)
    finnish_words = read_words_to_dict(finnish_file)

    finnish_file.close()
    english_file.close()

    print(len(finnish_words))
    print(len(english_words))

    count = 0

    """for finnish_word in finnish_words:
        if finnish_word in english_words:
            print(finnish_word)
            count += 1"""

    for w in finnish_words.keys():
        if w in english_words.keys():
            print(w)
            count += 1

    # count = len(intersection)

    print(str(count) + ' matches')

main()