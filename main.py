# -*- coding: utf8 -*-
import os


class Node(object):
    left = None
    right = None

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_leaves(self):
        return self.left, self.right


# подсчет частот символов, возхвращает словарь: {'a': 1, 'b': 2,...}
def count_symbols_and_frequency(path: str):
    file_list = os.listdir(path)
    symbol_freq = {}
    i = 1
    for file in file_list:
        with open(path + file) as f:
            for line in f:
                for s in line:
                    if s in symbol_freq:
                        symbol_freq[s] += 1
                    else:
                        symbol_freq[s] = 1
        i += 1
    return symbol_freq


# кодирование
def make_huffman_code(node: Node, binary_code=""):
    if type(node) is str:
        return {node: binary_code}
    (left, right) = node.get_leaves()
    d = {}
    if left is not None:
        d.update(make_huffman_code(left, binary_code + "0"))
    if right is not None:
        d.update(make_huffman_code(right, binary_code + "1"))
    return d


if __name__ == "__main__":
    path = "input/"
    symbols_and_freq = count_symbols_and_frequency(path)
    print("symbols_and_freq = ", symbols_and_freq)
    symbols_and_freq = sorted(symbols_and_freq.items(), key=lambda f: f[1], reverse=True)
    nodes_arr = symbols_and_freq
    print("nodes_arr = ", nodes_arr)

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
# TODO: параллельное чтение нескольких файлов
# TODO: вывод кода в CSV
