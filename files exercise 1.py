## Hapax Legomenon Exercise

import re


def hapax(filepath):
    book = open(filepath,'r',encoding="utf-8")
    words = re.findall('\w+', book.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print(word)
    return hapax

hapax('/Python Stuff/Algo Class Files/Algorithm-class-assignment/pg66688.txt')