"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1_000_000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать асинхронный код.
В каждом решении нужно вывести время выполнения вычислений.
"""

import random
import asyncio
import time

all_sum = 0


def get_array(size: int):
    return [random.randrange(1, 100) for _ in range(size)]


async def sum_array(array: [int]):
    global all_sum
    all_sum += sum(array)


arr = get_array(10_000_000)
t_start = time.time()
sum(arr)
t_end = time.time() - t_start
print(f'Время выполнения (синхрон): {t_end:0.3f} сек.')


async def main():
    time_start = time.time()

    task1 = asyncio.create_task(sum_array(arr[:len(arr) // 2]))
    task2 = asyncio.create_task(sum_array(arr[len(arr) // 2:]))

    await asyncio.gather(task1, task2)

    time_end = time.time() - time_start

    print(f'Общая сумма: {all_sum}')
    print(f'Время выполнения (асинхрон): {time_end:0.3f} сек.')


if __name__ == '__main__':
    asyncio.run(main())

# Синхронный код: 499946185
# Время выполнения (синхрон): 0.059 сек.
# Общая сумма: 499946185
# Время выполнения (асинхрон): 0.121 сек.
