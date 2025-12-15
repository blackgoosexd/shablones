from itertools import product

a = product('АЛПЦЯ', repeat = 5)
for i, z in enumerate(a):
    if 'Л' not in z:
        if sum(1 for j in z if j == 'Ц') == 2:
            if sum(1 for l in z if l == 'А') <= 1:
                print(i + 1, ''.join(z))




 #   https://education.yandex.ru/ege/inf/task/b3ba0f73-8f32-4ae0-be90-8b727190e93f