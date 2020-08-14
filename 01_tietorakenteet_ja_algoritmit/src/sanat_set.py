from wordfiles import get_finnish_words, get_english_words

def main():
    finnish = get_finnish_words()
    english = get_english_words()

    leikkaus = set(finnish) & set(english)
    count = len(leikkaus)

    for sana in leikkaus:
        print(sana)

    print(str(count) + ' matches')

main()