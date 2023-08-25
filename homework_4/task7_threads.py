"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность.
В каждом решении нужно вывести время выполнения вычислений.
"""

import threading
from random import randint as rnd
import time
import array as arr

arr_int = arr.array('i', [rnd(1, 100) for _ in range(1_000_000)])
sum_arr = 0


def sum_elem(from_: int):
    global sum_arr
    end_ = from_ + 100_000
    sum_arr += sum(arr_int[from_: end_])


threads_list = []
start = time.time()
for i in range(10):
    t = threading.Thread(target=sum_elem, args=(i,))
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()

print(f"Сумма элементов массива: {sum_arr}")
print(f"Время выполнения: {time.time() - start}")
