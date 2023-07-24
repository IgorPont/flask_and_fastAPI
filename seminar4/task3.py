"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого
адреса. После загрузки данных нужно записать их в отдельные файлы.
Используйте асинхронный подход.
"""

import asyncio
import aiohttp
import time

urls = ['https://www.python.org/',
        'https://www.ya.ru/',
        ]


# карутина
async def download(url: str) -> None:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open('website_pages/' + filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
