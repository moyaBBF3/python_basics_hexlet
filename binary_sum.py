def binary_sum(first_num, second_num):
    '''
    Функция принимает на вход два двоичных числа
    в виде строк и возвращает их сумму. Результат
    также должен быть бинарным числом в виде строки
    '''
    first_num = int(first_num, base=2)
    second_num = int(second_num, base=2)
    result = bin(first_num + second_num)
    return result[2:]


print(binary_sum('1', '1')) # 10
print(binary_sum('10', '1')) # 11
print(binary_sum('10', '10')) # 100
print(binary_sum('1101', '101')) # 10010
print(binary_sum('1111', '1111')) # 11110
