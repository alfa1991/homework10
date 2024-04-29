# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print("Параметр 'a':", a)
    print("Параметр 'b':", b)
    print("Параметр 'c':", c)
    print()

# Вызовы функции print_params с разным количеством аргументов
print("Вызов функции print_params без аргументов:")
print_params()
print("Вызов функции print_params с аргументом b = 25:")
print_params(b = 25)
print("Вызов функции print_params с аргументом c = [1,2,3]:")
print_params(c = [1, 2, 3])

# Распаковка параметров
values_list = [10, 'строка2', False]
values_dict = {'a': 100, 'b': 'строка3', 'c': True}

print("Вызов функции print_params с использованием распаковки параметров из списка:")
print_params(*values_list)

print("Вызов функции print_params с использованием распаковки параметров из словаря:")
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = ['новая строка', 99]

print("Вызов функции print_params с распакованным списком и дополнительным параметром 42:")
print_params(*values_list_2, 42)
