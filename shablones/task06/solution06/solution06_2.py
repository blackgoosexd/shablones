from turtle import *

screensize(3000, 3000)
tracer(0)
s = 25

for _ in range(2):
    fd(5 * s)
    lt(90)
    bk(13 * s)
    lt(90)
up()
bk(10 * s)
rt(90)
fd(9 * s)
lt(90)
down()
for _ in range(2):
    fd(11 * s)
    rt(90)
    fd(7 * s)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * s, y * s)
        dot(3, 'red')
done()
# https://education.yandex.ru/ege/inf/task/d792e650-8941-41fe-985b-82d8e3875f30