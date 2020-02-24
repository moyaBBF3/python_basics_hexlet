def fib(num):
    '''
    Функция находит положительные числа Фиббоначи.
    Аргументом функции является порядковый номер числа
    '''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(10)) # 55
