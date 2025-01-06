first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_resul = [word for word in first_strings if len(word) > 5]

second_result = [(word1, word2) for word1 in first_strings
                 for word2 in second_strings if len(word1) == len(word2)]

third_result = ({key: len(key) for key in first_strings if len(key) % 2 == 0} |
                {key: len(key) for key in second_strings if len(key) % 2 == 0})


print(first_resul)
print(second_result)
print(third_result)
