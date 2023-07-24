"""
Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить
результаты в консоль.
Используйте процессы.
"""

import multiprocessing
import os

PATH = '/'


def word_counter(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f_in:
        atm = len(f_in.read().split())
    print(f'{file_name} word: {atm}')


def main():
    processes = []
    for item in os.walk('.'):
        for pos in item[2]:
            file = os.path.join(item[0], pos)
            process = multiprocessing.Process(target=word_counter, args=(file,))
            processes.append(process)
            process.start()

        for thread in processes:
            thread.join()

        print('Finish')


if __name__ == '__main__':
    main()
