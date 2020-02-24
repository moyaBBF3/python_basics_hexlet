def fizz_buzz(begin, end):
    '''
    Функция возвращает строку с числами через пробел
    в диапазоне [begin, end]. Если диапазон пуст (begin > end) 
    возвращается пустая строка.
    Если число делится без остатка на 3, выводится слово Fizz
    Если число делится без остатка на 5, выводится слово Buzz
    Если число делится без остатка и на 3, и на 5, 
    выводится слово FizzBuzz
    В остальных случаях в строку добавляется само число.
    '''
    result = []
    for counter in range(begin, end + 1):
        if counter % 15 == 0:
            result.append("FizzBuzz")
        elif counter % 5 == 0:
            result.append("Buzz")
        elif counter % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(counter))
    return " ".join(result)


print(fizz_buzz(1, 100))
print(fizz_buzz(100, 1))
print(fizz_buzz(10, 50))
