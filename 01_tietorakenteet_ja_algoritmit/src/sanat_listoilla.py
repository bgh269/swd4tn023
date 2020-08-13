
def read_words_to_list(file):
    words = [] # luodaan tyhjä lista

    for line in file:
        word = line.strip() # poistetaan rivinvaihto
        words.append(word)  # lisätään sana sanalistaan

    return words            # palautetaan lista sanoineen

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
        if finnish_word in english_words:
            print(finnish_word)
            count += 1

    print(str(count) + ' matches')

main()