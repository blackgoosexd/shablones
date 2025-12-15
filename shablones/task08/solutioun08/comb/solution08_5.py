from itertools import product, repeat

sogl = 'БНДРЛ'
k = 0
for i in product('БАНДЕРОЛЬ', repeat = 7):
    if i.count('Ь') > 1:
        continue
    var = True
    for j in range(7):
        if i[j] == 'Е':
            if j > 0 and i[j - 1] in sogl:
                var = False
                break
            if j < 6 and i[j + 1] in sogl:
                var = False
                break

    if var:
        k += 1
print(k)

 #   https://education.yandex.ru/ege/inf/task/7ddd002e-129b-40c6-8fcf-431d15434fa8