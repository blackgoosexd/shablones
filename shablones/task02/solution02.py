print('y w z x')
 #фигачим все возможные булевые значения
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                 #   Пишем условие
                if ( w and (x == (z <= y)) ) == 1:
                     #   Принтуем 0\1
                    print(y, w, z, x)