from itertools import product

a1 = 'ЛОДКА'
a2 = 'ОКЛАД'
sogl = 'ДКЛ'
k = 0

a = product('АДКЛО', repeat = 5)

for i, z in enumerate(a):
    if 2410 < i < 2827: # их Id
        m = ''.join(z)
        if (m[2] == 'Д') and ( m[-2] in sogl ) and ( m.count('О') == 2):
            k += 1
print(k)
 #   Ещё приклоьный способ!
'''
from itertools import product

a1 = 'ЛОДКА'
a2 = 'ОКЛАД'
sogl = 'ДКЛ'
k = 0

a = product('АДКЛО', repeat=5)

found_a1 = False

for z in a:
    m = ''.join(z)
    
    if m == a1:
        found_a1 = True #   флаги зарешали

    if found_a1:
        if (m[2] == 'Д') and (m[-2] in sogl) and (m.count('О') == 2):
            k += 1
        
        if m == a2:
            break

print(k)
'''
 #   https://education.yandex.ru/ege/inf/task/de7eace6-8794-4d1b-b0fd-c7c42cff77d5