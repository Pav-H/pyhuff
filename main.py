# -*- coding: utf8 -*-
import csv
import os
import concurrent.futures


# класс - узел дерева
class Node(object):
    left = None
    right = None

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_leaves(self):
        return self.left, self.right


# чтение файла
def file_reading(file: str, d: dict):
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            for s in line:
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1


# подсчет частот символов, возвращает словарь: {'a': 1, 'b': 2,...}
def count_symbols_and_frequency(path: str):
    file_list = os.listdir(path)
    symbol_freq = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for file in file_list:
            futures.append(
                executor.submit(
                    file_reading, file=path + file, d=symbol_freq)
            )
        for future in concurrent.futures.as_completed(futures):
            future.result()
    return symbol_freq


# построение дерева, возвращает корень дерева
def make_tree(arr: []):
    while len(arr) > 1:
        (key1, c1) = arr[-1]
        (key2, c2) = arr[-2]
        arr = arr[:-2]
        node = Node(key1, key2)
        arr.append((node, c1 + c2))
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
    return arr[0][0]


# кодирование
def make_huffman_code(node: Node, binary_code=""):
    if type(node) is str:
        return {node: binary_code}
    (left, right) = node.get_leaves()
    code = {}
    if left is not None:
        code.update(make_huffman_code(left, binary_code + "0"))
    if right is not None:
        code.update(make_huffman_code(right, binary_code + "1"))
    return code


# запись кода в CSV файл
def make_csv(file: str, d):
    with open(file, 'w') as f:
        # с отключением автоцитирования, что бы не возникали лишние ковычки
        w = csv.writer(f, delimiter='|', quoting=csv.QUOTE_NONE, quotechar='')
        w.writerows(d.items())


if __name__ == "__main__":
    path = "input/"  # путь к файлам для чтения
    symbols_and_freq = count_symbols_and_frequency(path)
    # сортировка по ключам
    symbols_and_freq = sorted(symbols_and_freq.items(), key=lambda f: f[1], reverse=True)
    nodes_arr = symbols_and_freq

    nodes_arr = make_tree(nodes_arr)

    if nodes_arr.get_leaves is None:
        code = {nodes_arr: "0"}  # если во входных данных всего один сивол, то его код = 0
    else:
        code = make_huffman_code(nodes_arr)

    # вывод кода
    print("Char     Code")
    for (symbol, frequency) in symbols_and_freq:
        first, second = (symbol, code[symbol])
        print(first, " =    ", second)

    make_csv("output.csv", code)
