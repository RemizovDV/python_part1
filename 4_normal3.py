# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import re
import random

with open('test1.txt', 'w', encoding='UTF-8') as file:
    n = [str(random.randint(0, 9)) for _ in range(2499)]
    n = str(random.randint(1, 9)) + ''.join(n)
    file.write(n)

with open('test1.txt', 'r', encoding='UTF-8') as file:
    result = ['0']
    longnum = file.readline()
    pattern = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
              '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
    found = re.findall(pattern, longnum)
    [result.insert(0, x) for x in found if len(x) > len(result[0])]
    print(result.pop(0))
       
