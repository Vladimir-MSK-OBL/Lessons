import os
import time

directory = os.getcwd()
file1 = ''
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == 'with_operator.py':
            file1 = file

filepath = os.path.join(directory, file1)

filesize = os.path.getsize(file1)

filetime = os.path.getmtime(file1)

formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

parent_dir = os.path.dirname(directory)

print(
      f'Обнаружен файл: {file1},'
      f' Путь: {filepath},'
      f' Размер: {filesize} байт,'
      f' Время изменения: {formatted_time},'
      f' Родительская директория: {parent_dir}'
     )
