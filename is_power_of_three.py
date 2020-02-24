def is_power_of_three(number):
    '''
    Функция принимает число и определяет,
    является ли число натуральной степентю тройки
    '''
    if number:
        while number > 1:
            number /= 3
        if number == 1:
            return True
        return False
    return False


print(is_power_of_three(''))
print(is_power_of_three(1))
print(is_power_of_three(9))
print(is_power_of_three(17))
print(is_power_of_three(81))
print(is_power_of_three(19683)) # 3 ** 9

