# Функции работают с отрезками прямых на двумерной
# плоскости. Отрезок кодируется в виде пары пар и 
# выглядит так: ((x1, y1), (x2, y2)) 
# (вложенные пары — это концы отрезка)
# Реализовано четыре функции:


def is_degenerated(line):
    '''
    Функция возвращает истину, если 
    начало и конец совпадают
    '''
    (first_dot, second_dot) = line
    return first_dot == second_dot


def is_vertical(line):
    '''
    Функция возвращает истину, если 
    отрезок вертикальный
    '''
    ((x1, y1), (x2, y2)) = line
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    '''
    Функция возвращает истину, если 
    отрезок горизонтальный
    '''
    ((x1, y1), (x2, y2)) = line
    return y1 == y2 and x1 != x2


def is_inclined(line):
    '''
    Функция возвращает истину, если 
    открезок наклонный (не вертикальный
    и не горизонтальный)
    '''
    ((x1, y1), (x2, y2)) = line
    return x1 != x2 and y1 != y2


line = ((45, 102), (45, 102)) # is_degenerated
print(is_degenerated(line))
print(is_vertical(line))
print(is_horizontal(line))
print(is_inclined(line))
line2 = ((50, 5), (50, -5)) # is_vertical
print(is_degenerated(line2))
print(is_vertical(line2))
print(is_horizontal(line2))
print(is_inclined(line2))
print()
line3 = ((20, 10), (70, 10)) # is_horizontal
print(is_degenerated(line3))
print(is_vertical(line3))
print(is_horizontal(line3))
print(is_inclined(line3))
print()
line4 = ((5, 10), (15, 20)) # is_inclined
print(is_degenerated(line4))
print(is_vertical(line4))
print(is_horizontal(line4))
print(is_inclined(line4))
