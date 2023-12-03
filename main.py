my_dict = {}                                        # Создаем пустой словарь 

first_key = input('Введите первый ключ: ')          # Добавляем первый ключ
first_value = input('Введите перовое значение: ')   # Добавляем первое значение
my_dict[first_key] = first_value                    # Заполняем словарь первой парой ключ - значение

second_key = input('Введите второй ключ: ')         # Повторяем те же процедуры
second_value = input('Введите второе значение: ')   # еще 2 раза
my_dict[second_key] = second_value

third_key = input('Введите третий ключ: ')
third_value = input('Введите третье значение: ')
my_dict[third_key] = third_value

print(my_dict)                                      # Выводим словарь в консоль

my_dict['Mazda'] = 'Green'                          # Добавляем новый ключ

my_dict.pop('Honda')                                # Удаляем ключ

print(my_dict)