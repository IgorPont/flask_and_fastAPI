"""
Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить
результаты в консоль.
Используйте потоки.
"""

import threading
import os

PATH = '/'


def word_counter(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f_in:
        atm = len(f_in.read().split())
    print(f'{file_name} word: {atm}')


def main():
    threads = []
    for item in os.walk('.'):
        for pos in item[2]:
            file = os.path.join(item[0], pos)
            thread = threading.Thread(target=word_counter, args=(file,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print('Finish')


if __name__ == '__main__':
    main()
