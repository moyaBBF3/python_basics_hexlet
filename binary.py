def binary(decimal_num):
    '''
    Функция, которая возвращает двоичное представление
    десятичного числа в виде строки
    '''
    if not decimal_num:
        return '0'
    result = ''
    number = decimal_num
    while number:
        modulo = number % 2
        result = str(modulo) + result
        number = number // 2
    return result


print(binary(0))
print(binary(1))
print(binary(2))
print(binary(101))
print(binary(1024))
