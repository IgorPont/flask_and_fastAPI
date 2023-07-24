"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1_000_000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность
В каждом решении нужно вывести время выполнения вычислений.
"""

import random
import threading
import time

all_sum = 0


def get_array(size: int):
    return [random.randrange(1, 100) for _ in range(size)]


def sum_array(array: [int]):
    global all_sum
    all_sum += sum(array)


if __name__ == '__main__':
    arr = get_array(10_000_000)

    time_start = time.time()

    thread1 = threading.Thread(target=sum_array, args=[arr[:len(arr) // 2]])
    thread2 = threading.Thread(target=sum_array, args=[arr[len(arr) // 2:]])
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    time_end = time.time() - time_start

    print(f'Общая сумма: {all_sum}')
    print(f'Время выполнения: {time_end:0.3f} сек.')

# Общая сумма: 250005336
# Время выполнения: 0.213 сек.
