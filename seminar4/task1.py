"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого
адреса. После загрузки данных нужно записать их в отдельные
файлы. Используйте потоки.
"""
import threading
import requests

urls = [
    'https://www.google.com',
    'https://www.yandex.ru',
    'https://www.gb.ru',
]


def parse_urls(url: str):
    response = requests.get(url)
    file_name = f'parse_{url[7:].replace("/", "_")}.html'
    with open(file_name, "w", encoding='utf-8') as f_out:
        f_out.write(response.text)


def main():
    threads = []
    for url in urls:
        thread = threading.Thread(target=parse_urls, args=(url,))
        thread.start()
        threads.append(thread)

        for thread in threads:
            thread.join()

        print('Finish')


if __name__ == '__main__':
    main()
