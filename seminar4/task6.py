"""
Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить
результаты в консоль.
Используйте асинхронный подход.
"""

import asyncio
import os

PATH = '/'


async def word_counter(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f_in:
        atm = len(f_in.read().split())
    print(f'{file_name} word: {atm}')


async def main():
    tasks = []
    for item in os.walk('.'):
        for pos in item[2]:
            file = os.path.join(item[0], pos)
            task = asyncio.create_task(word_counter(file))
            tasks.append(task)

    await asyncio.gather(*tasks)

    print('Finish')


if __name__ == '__main__':
    asyncio.run(main())
