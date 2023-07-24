"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1_000_000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопроцессорность.
В каждом решении нужно вывести время выполнения вычислений.
"""

import random
import multiprocessing
import time

all_sum = multiprocessing.Value("i", 0)


def get_array(size: int):
    return [random.randrange(1, 100) for _ in range(size)]


def sum_array(array: [int], s):
    with s.get_lock():
        s.value += sum(array)


if __name__ == '__main__':
    arr = get_array(1_000_000)
    print(f'{sum(arr)}')

    time_start = time.time()

    process1 = multiprocessing.Process(target=sum_array, args=[arr[0:len(arr) // 2], all_sum])
    process2 = multiprocessing.Process(target=sum_array, args=[arr[len(arr) // 2:], all_sum])
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    time_end = time.time() - time_start

    print(f'Общая сумма: {all_sum}')
    print(f'Время выполнения: {time_end:0.3f} сек.')

# Общая сумма: <Synchronized wrapper for c_int(50043812)>
# Время выполнения: 0.369 сек.
