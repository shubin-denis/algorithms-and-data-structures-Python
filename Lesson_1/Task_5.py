# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a, b = input("Введите две буквы через пробел в диапозоне (a-z): ").split()
ma = ord(a) - ord('a') + 1
mb = ord(b) - ord('a') + 1
c = mb - ma - 1

print(f"Место первого символа в алфавите '{a}': {ma}")
print(f"Место второго символа в алфавите '{b}': {mb}")
print(f"Количество символов между ними: {c}")