import re


class WordsFinder:

    def __init__(self, *files):
        self.files = files
        self.file_names = []


    def file_list(self):
        for file in self.files:
            self.file_names.append(file)
        return self.file_names


    def get_all_words(self):

        all_words = {}

        for file in self.file_names:
            with open(file, encoding='UTF-8') as file_open:
                string = ''
                for line in file_open:
                    string += line.lower()

            clear_string = re.sub(r'[.,!?=:;-]', '', string)

            clear_string = clear_string.split(' ')

            values = []
            for value in  clear_string:
                values.append(value)

            all_words[file] = values

        return all_words


    def find(self, word):

        WordsFinder.file_list(self)

        word_dict = {}

        for name, words in WordsFinder.get_all_words(self).items():
            count = 0      # если отсчет с нуля, то счётчик установить в '-1'.
            for i in words:
                count += 1
                if i == word:
                    word_dict[name] = count

        return word_dict


    def count(self, word):

        WordsFinder.file_list(self)

        word_dict = {}

        for name, words in WordsFinder.get_all_words(self).items():
            _count = 0
            for i in words:
                if i == word:
                    _count += 1
                    word_dict[name] = _count

        return word_dict








wf = WordsFinder('test1.txt', 'test2.txt', 'test3.txt', 'test4.txt')

print(wf.file_list())
print(wf.get_all_words())

print(wf.find('рада'))
print(wf.count('рада'))