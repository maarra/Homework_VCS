# Funkce na sečtení textu v případě, že se nejedná o číslo
def secti_text(text):
    words = text.split()
    # print(words)
    # print(len(words))
    n_words = 0
    for _ in words:
        if not _.isnumeric():
            n_words += 1
            # print(_)
    return n_words

#Funkce nahradí původní slovo novým
def replace_word(text):
  old = input('\nType word to change: ')
  new = input('Type new word to replace: ')
  new_text = text.replace(old, new)
  return new_text


with open('lyrics.txt') as f:
    orig_lyrics = f.read()
print('>>> ORIGINAL LYRICS <<<')
print(orig_lyrics)

number_of_words = secti_text(orig_lyrics)
print(f'Number of non numeric words in original lyric: {number_of_words}')

new_text = replace_word(orig_lyrics)
print('\n<<< NEW EDITED LYRICS >>>')
print(new_text)
