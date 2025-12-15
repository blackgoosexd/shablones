from itertools import product

search = 'БЮДЖЕТ'
gl = ['Е', 'И', 'Ю']
sogl = ['Б', 'Д', 'Ж', 'Т', 'Н', 'К']
k = 0
a = product('БДЕЖИКТНЮ', repeat = 6)
for z, i in enumerate(a, start=1):
    flag = True
    m = ''.join(i)
    if m == search:
        break
    for j in range(len(m) - 1):
        if (m[j] in gl and m[j + 1] in gl) or ( m[j] in sogl and m[j + 1] in sogl):
            flag = False
            break
    if flag == True:
        k += z
print(k)


 #   https://education.yandex.ru/ege/inf/task/a835b02e-7ae7-480c-a0cf-866d4a013e09