def single_root_words(root_word, *other_words):

    same_words = []
    other_words_low = []
    root_word_low = ""

    for i in other_words:
        other_words_low.append(i.lower())

    root_word_low = root_word.lower()

    for j in other_words_low:
        if root_word_low in j:
            same_words.append(j)

    return same_words


result = single_root_words('rich', 'ricHiest', 'orichAlcum', 'cheErs', 'richies')
print(result)

result1 = single_root_words('able', 'Disablement', 'Mable', 'Disable', 'Bagel')
print(result1)