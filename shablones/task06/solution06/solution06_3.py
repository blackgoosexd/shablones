from turtle import *

screensize(3000, 3000)
tracer(0)
s = 25

rt(135)
for _ in range(7):
    fd(7 * s)
    rt(45)
    fd(8 * s)
    rt(135)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s,y * s)
        dot(4, 'red')
done()
# https://education.yandex.ru/ege/inf/task/c9ba8966-4156-4282-8657-b4f86e2a4cbd