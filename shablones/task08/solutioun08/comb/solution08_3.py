ch = '02468'
nech = '13579'
k = 0
for i in range(10000, 100000):
    a = str(i)
    if '5' in a:
        continue

    if len(a) != len(set(a)):
        continue
    valid = True
    for j in range(len(a) - 1):
        if (a[j] in ch and a[j+1] in ch) or (a[j] in nech and a[j+1] in nech):
            valid = False
            break
    if valid:
        k += 1
print(k)

 #   https://education.yandex.ru/ege/inf/task/ae97ab85-969c-401a-b0aa-38efd2a6ac5f