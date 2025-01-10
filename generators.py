def all_variants(text):

    for symbol in (text[0], text[1], text[2],
                   text[0:2], text[1:3], text
                   ):
        yield symbol



a = all_variants("abc")

for i in a:
    print(i)
