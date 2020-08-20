from wordfiles import get_finnish_words, get_english_words


def main():
    finnish_words = get_finnish_words()
    english_words = get_english_words()

    print(f'Suomenkielisiä sanoja on {len(finnish_words)}')
    print(f'Englanninkielisiä sanoja on {len(english_words)}')

    count = 0

    for finnish_word in finnish_words:
        if finnish_word in english_words:
            print(finnish_word)
            count += 1

    print(f'{count} matches')


main()
