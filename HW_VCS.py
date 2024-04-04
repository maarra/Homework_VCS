# Funkce na sečtení textu v případě, že se nejedná o číslo
def secti_text(text):
    words = text.split()
    # print(words)
    print(len(words))
    n_words = 0
    for _ in words:
        if not _.isnumeric():
            n_words += 1
            print(_)
    print(n_words)


with open('lyrics.txt') as f:
    lyrics = f.read()
secti_text(lyrics)

