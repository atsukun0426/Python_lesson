# -*- coding: utf-8 -*-
list = [(x, y) for x in 'abc' for y in range(1, 3)]

print(list)

list_a = [[1, 2, 3], ['a', 'b', 'c'], ['い', 'ろ', 'は']]
list_b = [row[0] for row in list_a]

print(list_b)

list_a = [[1,2,3],['a','b','c'],['い','ろ','は']]
list_b = [[row[i] for row in list_a] for i in range(3)]
print(list_b)

