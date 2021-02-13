def get_summ(one, two, delimiter='&'):
    ''' Первое задание с функцией

    Три аргумента. Вывод заглавными буквами'''
    return f'{one} {delimiter} {two}'.upper()

enter = get_summ('Learn','python')
print(enter)
