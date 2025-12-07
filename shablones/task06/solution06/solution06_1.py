from turtle import *

screensize(3000, 3000)
tracer(0)

s = 25
down()
for _ in range(7):
    rt(90)
    fd(7 * s)
    rt(90)
    fd(6 * s)
up()
rt(90)
fd(3 * s)
rt(90)
fd(1 * s)
down()
for _ in range(4):
    rt(90)
    fd(6 * s)
    rt(90)
    fd(11 * s)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')
done()
# https://education.yandex.ru/ege/inf/task/4c294fbf-9491-43e8-aedb-30aa70f9de99
# КОНЧЕННОЕ условие для ответа! / 74