x = 50


def func():
    global x

    print('x равно', x)
    x = 2
    print('Заменияем глобальное значение x на', x)


func()
print('Значение x составляет', x)
