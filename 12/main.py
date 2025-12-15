from math import inf
from typing import Dict, Optional
import random

def minVal(list_: list[int]) -> Optional[Dict[str, int]]:
    min_value = inf
    dict_tmp = {}
    iterator = 0

    for iterator, el in enumerate(list_):
        if type(el) is list:
            for el_ in el:
                if min_value >= el_:
                    min_value = el_
                    dict_tmp.update({iterator: {'index': el.index(el_), 'element': el_}})
                    
        else:
            if min_value >= el:
                min_value = el
                dict_tmp.update({iterator: {'index': list_.index(el), 'element': el}})    
                print(dict_tmp)
    min_k_element = min(dict_tmp, key=lambda k: dict_tmp[k]["element"])
    min_k_index = min(dict_tmp, key=lambda k: dict_tmp[k]["index"])
    print(dict_tmp)
    if dict_tmp[min_k_element]['element'] == dict_tmp[min_k_index]['element']:
        dicr_r = {
            'index': dict_tmp[min_k_index]['index'],
            'value': dict_tmp[min_k_index]['element']
            }
    else:
        dicr_r = {
            'index': dict_tmp[min_k_element]['index'],
            'value': dict_tmp[min_k_element]['element']
            }
    return dicr_r

rows, cols = map(int, input("столбцы столбы: ").split())
i = 0
ans = False
numbers = []
while i <= cols:
    i +=1
    numbers.append([random.randint(0, 5) for i in range(rows)])



matrix = [[2, 3, 2, 2, 1],
 [5, 5, 2, 4, 2],
 [2, 5, 3, 0, 2],
 [3, 4, 0, 1, 0],
 [0, 1, 2, 3, 0],
 [4, 5, 4, 4, 4]]
print(matrix)
result = minVal(matrix)
print(f"столб {result.get('index')}, значение {result.get('value')}")


