# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

start_code = 32
end_code = 127
count = start_code

while count <= end_code:
    if not (count - start_code) % 10:
        print()
    print(f'{count:3d}-{chr(count)} ', end="")
    count += 1
