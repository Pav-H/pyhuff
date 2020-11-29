# -*- coding: utf8 -*-

# print("Enter a string")
# str_in = input()
str_in = "aaabbccd aabbcd"

letters_and_freq = []  # символы и их частота [a, 1, b, 2,...]
letters_used = []  # используемые символы
for symbol in str_in:
    if symbol not in letters_and_freq:
        frequency = str_in.count(symbol)
        letters_and_freq.append(frequency)
        letters_and_freq.append(symbol)
        letters_used.append(symbol)
print("letters_and_freq = ", letters_and_freq)
print("letters_arr = ", letters_used)

nodes = []  # список узлов [ [a,1], [b, 2],... ]
while len(letters_and_freq) > 0:
    nodes.append(letters_and_freq[0:2])
    letters_and_freq = letters_and_freq[2:]
nodes.sort()
print("nodes after sort", nodes)
tree = [nodes]


# обьединение узлов в дерево и установка пометок 0 и 1 каждой паре узлов
def combine_nodes(nodes):
    position = 0
    new_node = []
    if len(nodes) > 1:
        nodes.sort()
        nodes[position].append("0")
        nodes[position + 1].append("1")
        combined_node1 = (nodes[position][0] + nodes[position + 1][0])
        combined_node2 = (nodes[position][1] + nodes[position + 1][1])
        # print("combined_node1 = ", combined_node1)
        # print("combined_node2 = ", combined_node2)
        new_node.append(combined_node1)
        new_node.append(combined_node2)
        # print("new_node.append = ", new_node)
        new_node_arr = [new_node]
        new_node_arr = new_node_arr + nodes[2:]
        # print("new_node_arr = ", new_node_arr)
        nodes = new_node_arr
        tree.append(nodes)
        # print("tree.append = ", tree)
        # print()
        combine_nodes(nodes)
    return tree


new_nodes = combine_nodes(nodes)
tree.sort(reverse=True)
print("tree.sort = ", tree)

# удаление дубликатов
count_arr = []
for tier in tree:  # ярус
    for node in tier:  # узел
        if node not in count_arr:
            count_arr.append(node)
        else:
            tier.remove(node)
print("tree after del = ", tree)

# вывод дерева
print()
count = 0
for tier in tree:
    print("tier", count, " = ", tier)
    count += 1

# кодирование
binary_code = []
if len(letters_used) == 1:
    code_letter = [letters_used[0], "0"]
    binary_code.append(code_letter * len(str_in))
else:
    for symbol in letters_used:
        code_symbol = ""
        for node in count_arr:
            if len(node) > 2 and symbol in node[1]:
                code_symbol = code_symbol + node[2]
        code_letter = [symbol, code_symbol]
        binary_code.append(code_letter)

# вывод кодов для символов
print()
print("symbol   code")
for symbol_code in binary_code:
    print(symbol_code[0], "      ", symbol_code[1])
