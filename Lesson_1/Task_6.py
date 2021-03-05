# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


position_of_letter = input('Введите позицию буквы в алфавите: ')

try:
    position_of_letter = int(position_of_letter)
    if 1 <= position_of_letter <= 26:
        letter_in_position = chr(position_of_letter + 96)
        print(f'Буква алфавита на данной позиции - {letter_in_position}')
    else:
        raise NameError
except (NameError, ValueError):
    print('Введена неверная позиция')
