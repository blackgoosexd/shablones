from itertools import product

a = product("АИМРЯ", repeat = 4)
for i, z in enumerate(a):
    if ''.join(z) == 'АРИЯ':
        print(i + 1)

 #   https://education.yandex.ru/ege/inf/task/e73090d1-5401-4307-8b8c-bd1af02cefc0