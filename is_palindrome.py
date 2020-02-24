def is_palindrome(input_word):
    '''
    Функция принимает слово, определяет, является ли оно
    палиндромом и возвращает логическое значение
    '''
    input_word = input_word.lower()
    if input_word == input_word[::-1]:
        return True
    return False


print(is_palindrome('Tenet'))
print(is_palindrome('Racecar'))
print(is_palindrome('Refer'))
print(is_palindrome('Excellent'))
print(is_palindrome('Wonderful'))
