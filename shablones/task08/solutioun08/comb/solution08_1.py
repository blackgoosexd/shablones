from itertools import product
k=0
for i in product('0123456', repeat = 6):
    m = ''.join(i)
    if i[0] in '246':
        if m.count('5') == 2:
            k += 1
print(k)

  #   https://education.yandex.ru/ege/inf/task/32201764-f33f-4f06-afd2-1bf4f34ce6d0