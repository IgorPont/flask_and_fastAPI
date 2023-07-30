"""
Многопоточная загрузка файлов
"""
import os.path
import threading
import requests


def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        filename = url.rsplit('/', 1)[-1]
        filename = os.path.join('images', filename)
        with open(filename, 'wb') as f:
            f.write(content)
        print(f'Загружен файл {filename}')


def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    urls = ['https://img.freepik.com/premium-photo/a-chimpanzee-in-a-suit-with-a-tie_727939-7105.jpg',
            ]
    main(urls)
