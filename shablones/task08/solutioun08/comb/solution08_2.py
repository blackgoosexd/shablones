from itertools import product

k = 0
flag = True
for x in product('012345', repeat = 6):

    m = ''.join(x)
    if m[0] == '0':
        continue
    if m.count('2') != 1:
        continue
    i = x.index('2')

    flag = False

    if i > 0 and m[i-1] in '135':
        flag = True
    if i < 5 and m[i + 1] in '135':
        flag = True

    if not flag:
        k += 1
print(k)

 #   https://education.yandex.ru/ege/inf/task/b19825e6-aafc-48ed-9bd7-99033090c53c