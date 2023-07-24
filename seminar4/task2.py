"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого
адреса. После загрузки данных нужно записать их в отдельные файлы.
Используйте процессы.
"""

import multiprocessing
import requests

urls = [
    'https://www.google.com',
    'https://www.yandex.ru',
    'https://www.gb.ru',
]


def parse_urls(url: str):
    response = requests.get(url)
    file_name = f'processes_{url[8:].replace("/", "_")}.html'
    with open(file_name, "w", encoding='utf-8') as f_out:
        f_out.write(response.text)


def main():
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=parse_urls, args=(url,))
        process.start()
        processes.append(process)

        for process in processes:
            process.join()

        print('Finish')


if __name__ == '__main__':
    main()
