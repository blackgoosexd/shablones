from itertools import product

gl = ['И', 'Ю']
sp = []

a = product('ИНЬЮ', repeat = 5)
for z, i in enumerate(a):
    yep1 = sum(1 for j in i if j in gl)
    if yep1 == 2:
        print(z + 1, ''.join(i)) #   ПРОСТО КОНЧЕННЫЙ ОТСЧЁТ С 1!!!

 #   https://education.yandex.ru/ege/inf/task/ddc54ae6-f1ac-46ef-8a7b-15dd11634375