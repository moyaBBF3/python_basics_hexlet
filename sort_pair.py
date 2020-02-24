def sort_pair(pair):
    '''
    Функция принимает кортеж из двух значений (пару)
    и возвращает пару, значения которой расположены
    строго в порядке возрастания
    '''
    (first_value, second_value) = pair
    if first_value > second_value:
        return (second_value, first_value)
    return pair


print(sort_pair((10, 1)))
print(sort_pair((3, 3)))
print(sort_pair((8, 7)))
print(sort_pair((1, 2)))
