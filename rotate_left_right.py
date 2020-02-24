def rotate_left(value):
    '''
    Функция "вращает" кортеж-тройку влево.
    '''
    (one, two, three) = value
    return (two, three, one)


def rotate_right(value):
    '''
    Функция "вращает" кортеж-тройку вправо
    '''
    (one, two, three) = value
    return (three, one, two)


value = ('A', 'B', 'C')
print(rotate_left(value))
print(rotate_right(value))
