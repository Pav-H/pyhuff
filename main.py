# -*- coding: utf8 -*-
import os
import concurrent.futures


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


# подсчет частот символов, возхвращает словарь: {'a': 1, 'b': 2,...}
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


if __name__ == "__main__":
    path = "input/"

    symbols_and_freq = count_symbols_and_frequency(path)
    print("symbols_and_freq = ", symbols_and_freq)

    symbols_and_freq = sorted(symbols_and_freq.items(), key=lambda f: f[1], reverse=True)
    nodes_arr = symbols_and_freq
    print("nodes_arr = ", nodes_arr)

    # построение дерева
    while len(nodes_arr) > 1:
        (key1, c1) = nodes_arr[-1]
        (key2, c2) = nodes_arr[-2]
        nodes_arr = nodes_arr[:-2]
        node = Node(key1, key2)
        nodes_arr.append((node, c1 + c2))
        nodes_arr = sorted(nodes_arr, key=lambda x: x[1], reverse=True)

    if nodes_arr[0][0].get_leaves is None:
        code = {nodes_arr[0][0]: "0"}  # если строка из одного символа
    else:
        code = make_huffman_code(nodes_arr[0][0])
    print("code = ", code)
    print("Char     Code")

    for (symbol, frequency) in symbols_and_freq:
        first, second = (symbol, code[symbol])
        print(first, " =    ", second)

# TODO: unittest
# TODO: вывод кода в CSV
