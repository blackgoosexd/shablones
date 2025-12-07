from turtle import *

screensize(3000, 3000)
tracer(0)
s = 25

lt(40)
for _ in range(5):
    lt(95)
    fd(12 * s)
    lt(45)
    fd(8 * s)
    lt(40)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')
done()
# https://education.yandex.ru/ege/inf/task/9cf4b3b6-bed0-4c41-99fe-c1f6b8c80b19