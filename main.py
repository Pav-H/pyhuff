# -*- coding: utf8 -*-


class Node(object):
    left = None
    right = None

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_leaves(self):
        return self.left, self.right


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
    str_in = "aaabbccd aabbcd"
    symbols_and_freq = {}  # символы и их частота {'a': 1, 'b': 2,...}
    for symbol in str_in:
        if symbol in symbols_and_freq:
            symbols_and_freq[symbol] += 1
        else:
            symbols_and_freq[symbol] = 1
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

# TODO: чтение из файлов
# TODO: использовать multiprocessing для параллельной обработки нескольких файлов
