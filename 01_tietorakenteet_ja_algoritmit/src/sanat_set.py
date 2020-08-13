def read_words(path):
    with open(path, encoding='utf-8') as file:
        return set(file.read().splitlines())

def main():
    finnish_words = read_words('kotus-sanalista-suomi.txt')
    english_words = read_words('englanti-UNLICENSED.txt')

    leikkaus = finnish_words & english_words
    count = len(leikkaus)

    for sana in leikkaus:
        print(sana)

    print(str(count) + ' matches')

main()