from itertools import product
k = 0
for i in product('0123', repeat = 4):
    if len(set(i)) < 4 and i[0] != '0':
        k += 1

print(k)

 #   https://education.yandex.ru/ege/inf/task/e327b270-8faa-450f-a350-e313a28bbee9