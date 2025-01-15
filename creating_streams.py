import threading
import time
from time import sleep


def write_words(word_count, file_name):

    with open(file_name, 'a', encoding='UTF-8') as file_open:

        for number in range(1, word_count + 1):
            file_open.write(f'Какое-то слово № {number}\n')

            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()

write_words(10, 'exemple1.txt')
write_words(30, 'exemple2.txt')
write_words(200, 'exemple3.txt')
write_words(100, 'exemple4.txt')

end_time = time.time()
print(f'Работа потоков {end_time - start_time}')


start_time = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'exemple5.txt'))
thread_1.start()

thread_2 = threading.Thread(target=write_words, args=(30, 'exemple6.txt'))
thread_2.start()

thread_3 = threading.Thread(target=write_words, args=(200, 'exemple7.txt'))
thread_3.start()

thread_4 = threading.Thread(target=write_words, args=(100, 'exemple8.txt'))
thread_4.start()
thread_3.join()

end_time = time.time()
print(f'Работа потоков {end_time - start_time}')