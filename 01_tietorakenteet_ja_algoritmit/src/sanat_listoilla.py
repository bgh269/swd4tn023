from wordfiles import get_finnish_words, get_english_words


def main():
    finnish_words = get_finnish_words()
    english_words = get_english_words()

    print("Suomenkielisiä sanoja on {0}".format(len(finnish_words)))
    print("Englanninkielisiä sanoja on {0}".format(len(english_words)))

    count = 0

    for finnish_word in finnish_words:
        if finnish_word in english_words:
            print(finnish_word)
            count += 1

    print(str(count) + ' matches')


main()
