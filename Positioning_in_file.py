
def custom_write(file_name, strings):

    line_num = 0
    strings_positions = {}

    file = open(file_name, 'a', encoding='UTF-8')

    for value in strings:
        begin_line = (file.tell())
        file.write (value + '\n')
        line_num += 1
        key = ()
        key += (line_num,)
        key += (begin_line,)
        strings_positions[key] = value

    file.close()

    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
       ]

file1 = 'test.txt'

s = custom_write(file1, info)
print(s)