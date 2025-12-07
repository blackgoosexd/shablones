# от джобсика))
from turtle import *

screensize(3000, 3000)
tracer(0)
s = 25

for _ in range(15):
    for i in range(20):
        fd(40 * s)
        rt(90)
    lt(90)
up()
for x in range(0, 40): # положительными координатами
    for y in range(0, 40): # положительными координатами
        goto(x * s,y * s)
        dot(4, 'red')
done()
# https://education.yandex.ru/ege/inf/task/c6d8a84e-640e-40c0-a97d-2569546ec12f