from pathlib import Path

def read_words(filename):
    file_path = Path(__file__).parent/filename # https://stackoverflow.com/a/52266636
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()

def get_finnish_words():
    return read_words('kotus-sanalista-suomi.txt')

def get_english_words():
    return read_words('englanti-UNLICENSED.txt')
