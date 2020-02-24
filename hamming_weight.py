def hamming_weight_first(number):
    '''
    Функция принимает число и считает вес Хэмминга.
    Вес Хэмминга - это количество единиц 
    в двоичном представлении числа.
    '''
    return (bin(number).count('1'))


def hamming_weight_second(input_number):
    weight = 0
    binary_num = bin(input_number)[2:]
    for number in binary_num:
        weight += int(number)
    return weight


print(hamming_weight_first(0)) # 0b0
print(hamming_weight_first(4)) #0b100 
print(hamming_weight_first(15)) #0b1111
print()
print(hamming_weight_second(10)) # 0b1010
print(hamming_weight_second(12)) # 0b1100
print(hamming_weight_second(16)) # 0b100000
