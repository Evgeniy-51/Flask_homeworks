"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопроцессорность.
В каждом решении нужно вывести время выполнения вычислений.
"""
import multiprocessing
from random import randint as rnd
import time
import array as arr

arr_int = arr.array('i', [rnd(1, 100) for _ in range(1_000_000)])


def sum_elem(args):
    from_ = args[0]
    end_ = from_ + 100_000
    return sum(arr_int[from_: end_])


if __name__ == '__main__':
    proc_list = []
    pool = multiprocessing.Pool(processes=2)
    for i in range(10):
        proc_list.append((i * 100_000,))
    start = time.time()
    res_list = pool.map(sum_elem, proc_list)
    print(f"Сумма элементов массива: {sum(res_list)}")
    print(f"Время выполнения: {time.time() - start}")
